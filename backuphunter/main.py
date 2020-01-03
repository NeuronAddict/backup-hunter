import argparse
import requests

from backuphunter.search import search


def main():
    parser = argparse.ArgumentParser(description='Find backup files on web application.\n'
                                     'For each URL, search variations for backup files.\n'
                                     'Example : for index.php, search index.php~,index.php.bak, index.bak...',
                                     epilog='Bugs, questions, say hello : '
                                     'https://github.com/NeuronAddict/backup-hunter.')
    parser.add_argument('--url', help='URL of a file to search backup.')
    parser.add_argument('--urls_file',
                        help='File containing a list of urls to test, use a hyphen (-) to read from stdin.\n'
                             'Take precedence to --url.')
    parser.add_argument('--verbose', action='store_true', help='Verbose mode, you will see all called urls')
    parser.add_argument('--proxy', help='Proxy to use. Great for see exactly what append on network ;)')
    parser.add_argument('--cookie', help='Cookie to use')
    parser.add_argument('--template', help='Override the template file')
    parser.add_argument('--user-agent', help='Custom user-agent')

    args = parser.parse_args()
    try:
        search(args)
        return 0
    except requests.exceptions.ConnectionError as e:
        print(e)
        return 1
    except Exception as e:
        print(e)
        return 2
