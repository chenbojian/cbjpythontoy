import subprocess as sp
from pathlib import Path


def first_exist_path(paths):
    for path in paths:
        if Path(path).exists():
            return path
    raise Exception()


def find_seven_zip():
    paths = [r'C:\7z.exe', r'C:\Program Files\7-Zip\7z.exe']
    return first_exist_path(paths)


class SevenZip(object):
    def __init__(self):
        self.exe = find_seven_zip()

    def list_zipped_file(self, file, password=None):
        process = sp.Popen([self.exe, 'l', file], stdin=sp.PIPE, stdout=sp.PIPE)
        if password is not None:
            process.stdin.write(password.encode('gbk'))
            process.stdin.close()
        output = process.stdout.read()
        process.wait()
        return output

    def unzip_zipped_file(self, file, password=None):
        process = sp.Popen([self.exe, 'x', file], stdin=sp.PIPE, stdout=sp.PIPE)
        if password is not None:
            process.stdin.write(password.encode('gbk'))
            process.stdin.close()
        output = process.stdout.read()
        process.wait()
        return output
