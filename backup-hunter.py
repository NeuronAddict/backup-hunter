#! /usr/bin/env python3

import argparse
import sys

import requests

from template import Template
from url_extract import split_file
from url_test import test_url

parser = argparse.ArgumentParser('Find backup files on web application.\n'
                                 'Help, bugs, questions, say hello : https://github.com/NeuronAddict/backup-hunter.')
parser.add_argument('--url', help='URL of a file to search backup.')
parser.add_argument('--urls_file', help='File containing a list of urls to test, use a hyphen (-) to read from stdin\n'
                    'Take precedence to --url.')
parser.add_argument('--verbose', action='store_true', help='Verbose mode, you will see all called urls')
parser.add_argument('--proxy', help='Proxy to use. Great for see exactly what append on network ;)')
parser.add_argument('--cookie', help='Cookie to use')
parser.add_argument('--template', help='Override the template file')

args = parser.parse_args()

if args.template:
    template = Template(args.template)
else:
    template = Template('template.txt')


session = requests.session()
if args.proxy:
    session.proxies = {'http': args.proxy, 'https': args.proxy}
if args.cookie:
    session.headers = {'Cookie': args.cookie,
                       'User-Agent': 'Backup Hunter https://github.com/NeuronAddict/backup-hunter'}


def search_variations(url):
    if len(url) > 0:
        base, fullname = split_file(url)
        for variation in template.variations(fullname, args.verbose):
            test_url(base + '/' + variation, session, args.verbose)


if args.urls_file:
    if args.urls_file == '-':
        for url in sys.stdin:
            search_variations(url.rstrip())
    else:
        with open(args.urls_file) as file:
            for line in file:
                search_variations(line.rstrip())
else:
    if args.url:
        search_variations(args.url)
    else:
        print('[-] You should use at least --url or --urls_file.')
