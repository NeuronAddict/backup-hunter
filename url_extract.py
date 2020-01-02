from urllib.parse import urlparse, unquote

def split_file(url):
    parsed = urlparse(url)

    if(parsed.path.endswith('/')):
        raise Exception('This url is not a file, its a dir or implicit index file '
                        '(try to find the file, index.php for example)')


    index = parsed.path.rfind('/')
    base = parsed.path[:index]
    fullname = parsed.path[index + 1:]

    return parsed.scheme + '://' + parsed.netloc + base, fullname