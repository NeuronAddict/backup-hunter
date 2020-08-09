# backup-hunter
Find backup files on a web application.


## installation

```
git clone https://github.com/NeuronAddict/backup-hunter.git
cd backup-hunter
pip install .
python3 -m backup-hunter --help
```

## example

(need https://docs.docker.com/compose/)

```
backup-hunter$ cd itests/docker
backup-hunter$ docker-compose up
backup-hunter$ python3 -m backuphunter --url http://localhost:8000/index.php
[+] found accessible file : http://localhost:8000/index-bak.php (200)
[+] found accessible file : http://localhost:8000/index.bak.php (200)
backup-hunter$ echo '\o/'
```

## help

```
usage: __main__.py [-h] [--url URL] [--urls_file URLS_FILE] [--verbose]
                   [--proxy PROXY] [--cookie COOKIE] [--template TEMPLATE]
                   [--user-agent USER_AGENT]

Find backup files on web application. For each URL, search variations for
backup files. Example : for index.php, search index.php~,index.php.bak,
index.bak...

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL of a file to search backup.
  --urls_file URLS_FILE
                        File containing a list of urls to test, use a hyphen
                        (-) to read from stdin. Take precedence to --url.
  --verbose             Verbose mode, you will see all called urls
  --proxy PROXY         Proxy to use. Great for see exactly what append on
                        network ;)
  --cookie COOKIE       Cookie to use
  --template TEMPLATE   Override the template file
  --user-agent USER_AGENT
                        Custom user-agent

Bugs, questions, say hello : https://github.com/NeuronAddict/backup-hunter.
```