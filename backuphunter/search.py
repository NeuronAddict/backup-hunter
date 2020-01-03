import os
import sys

import requests

from backuphunter.template import Template
from backuphunter.url_extract import split_file
from backuphunter.url_test import check_url


def search_variations(url, session, template, verbose):
    found = []
    if len(url) > 0:
        base, fullname = split_file(url)
        for variation in template.variations(fullname, verbose):
            to_test = base + '/' + variation
            if check_url(to_test, session, verbose):
                found.append(to_test)
    return found


def search(args):

    template = get_template(args)
    session = get_session(args)

    found = []
    if args.urls_file:
        if args.urls_file == '-':
            for url in sys.stdin:
                url = url.rstrip()
                for find in search_variations(url, session, template, args.verbose):
                    found.append(find)
        else:
            with open(args.urls_file) as file:
                for line in file:
                    line = line.rstrip()
                    for find in search_variations(line, session, template, args.verbose):
                        found.append(find)
    else:
        if args.url:
            found = search_variations(args.url, session, template, args.verbose)
        else:
            print('[-] You should use at least --url or --urls_file.')
    return found


def get_session(args):
    session = requests.session()
    if args.proxy:
        session.proxies = {'http': args.proxy, 'https': args.proxy}
    if args.cookie:
        session.headers = {'Cookie': args.cookie}
    if args.user_agent:
        session.headers['User-Agent'] = args.user_agent
    else:
        session.headers['User-Agent'] = 'Backup Hunter https://github.com/NeuronAddict/backup-hunter'
    return session


def get_template(args):
    if args.template:
        template = Template(args.template)
    else:
        dir = os.path.dirname(__file__)
        template = Template(os.path.join(dir, 'template.txt'))
    return template
