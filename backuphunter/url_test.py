from termcolor import colored


def check_url(url, session, verbose):
    if verbose:
        print('[*] try url {}'.format(url))

    r = session.head(url, verify=False)

    if r.status_code == 200:
        print(colored('[+] found accessible file : {} ({})'.format(url, r.status_code), 'green'))
        return True
    else:
        if r.status_code < 400:
            print(colored('[+] found a response for file {} ({})'.format(url, r.status_code), 'green'))
            return True
        else:
            if r.status_code >= 500:
                print('[*] Error for file {} ({})'.format(url, r.status_code))
                return False
            else:
                if verbose:
                    print(colored('[-] nothing for {} ({})'.format(url, r.status_code), 'red'))
                    return False
