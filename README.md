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

```
. .env
```

Run
```
./main.sh
```