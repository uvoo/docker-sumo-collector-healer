# To install and run in bash

Install ansible
```
apt install ansible
```
use dnf or yum install ansible if RHEL based

Download
```
git clone https://github.com/uvoo/docker-sumo-collector-healer.git
cd docker-sumo-collector-healer 
```

Copy example .env
```
cp .env.example .env
```

Then edit .env and set your personal preferences
```
nano .env
```

Set environment variables in bash
```
. .env
```

Run service which loops depending on INTERVAL
```
./main.sh
```

Single Example with .env set to your environment
```
. .env
envsubst < vars.yaml.envsubst > vars.yaml
ansible-playbook -i myhostoripaddr, playbookSumoCollector.yaml
```
