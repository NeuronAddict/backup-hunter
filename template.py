import os


class Template(object):

    def __init__(self, template_file):
        self.lines = []
        with open(template_file) as file:
            for line in file:
                line = line.rstrip()
                if self.is_code(line):
                    self.lines.append(line)

    def variations(self, fullname, verbose=False):
        ret = []
        filename, extension = os.path.splitext(fullname)
        if len(extension) > 0 and extension[0] == '.':
            extension = extension[1:]
        for line in self.lines:
            if verbose:
                print('[*] {} -> {},{} against {}'.format(fullname, filename, extension, line))
            ret.append(self.variation(filename, extension, fullname, line))
        return ret

    @staticmethod
    def is_code(line):
        line = line.rstrip()
        return len(line) > 0 and line[0] != '#'

    @staticmethod
    def variation(filename, extension, fullname, line):
        return line.replace('{extension}', extension) \
            .replace('{filename}', filename) \
            .replace('{fullname}', fullname)
