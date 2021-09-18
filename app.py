#!/usr/bin/env python3
import argparse
import ipaddress
import json
import os
import pprint
import socket
from subprocess import PIPE, run, call, check_output
import subprocess
import sys
import time

import requests
from requests.auth import HTTPBasicAuth

SUMO_ACCESS_ID = os.environ.get("SUMO_ACCESS_ID")
SUMO_ACCESS_KEY = os.environ.get("SUMO_ACCESS_KEY")
SUMO_URL = os.environ.get("SUMO_URL")
inventory_file = ".inventory.yaml"


def get_stopped_collectors(domain):
    r = requests.get(SUMO_URL, auth=HTTPBasicAuth(SUMO_ACCESS_ID, SUMO_ACCESS_KEY))
    hosts = []
    if r.status_code != 200:
        print("ERROR: API 401: Invalid auth? Check user/pass or api token combo.")
        return 1
    items = r.json()['collectors']
    for item in items:
        host = item['name'].replace('_events', '')
        host = f"{host}.{domain}"
        alive = item['alive']

        if test_is_valid_host_or_ipaddr(host) != 0:
          continue
        if(alive != False):
            continue
        try:
            os = ""
            os = item['osName']
        except:
            continue
        if "windows" in os.lower():
            print(host)
            hosts.append(host)
        elif "linux" in os.lower():
            pass
        else:
            pass
            # print(f"{host} appears to be down or os is not unsupported.")
            continue
    create_ansible_inventory(hosts)


def create_ansible_inventory(hosts):
    txt = ("all:\n"
          "  hosts:\n"
          )
    for host in hosts:
        txt = txt + f"    {host}:\n"
    with open(inventory_file, 'w') as f:
        f.write(txt)


def test_is_valid_host_or_ipaddr(host):
    try:
        ipaddress.ip_address(host)
        return 0
    except:
        pass
    try:
        socket.gethostbyname(host)
        return 0
    except:
        # print(f"E: {host} is not valid ip address or can't be resolved!")
        return 1


def main():
    parser = argparse.ArgumentParser(description='Run systems service checker.')
    parser.add_argument('-i', '--interval-in-seconds', required=True, type=int,
                        help='Interval in seconds to check sumologic.com and try and restart service with "Stopped Collector" status.')
    parser.add_argument('-d', '--domain', required=True, type=str,
                        help='Domain of hosts')
    args = parser.parse_args()
    while True:
        get_stopped_collectors(args.domain)
        r = run([f"ansible-playbook -i {inventory_file} playbookSumoCollector.yaml"],
                 shell=True, stdout=PIPE, stderr=PIPE)
        print(r)
        print(f"Waiting {args.interval_in_seconds} seconds for next loop.")
        time.sleep(args.interval_in_seconds)


if __name__ == "__main__":
    main()
