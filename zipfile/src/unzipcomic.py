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


def generate_args(**kwargs):
    sequence = ['exe', 'action', 'destination', 'password', 'file']
    sequence = list(filter(lambda x: x in kwargs.keys(), sequence))
    if 'password' in sequence:
        kwargs['password'] = '-p' + kwargs['password']
    if 'destination' in sequence:
        kwargs['destination'] = '-o' + kwargs['destination']
    return list(map(lambda key: kwargs[key], sequence))


class SevenZip(object):
    def __init__(self):
        self.exe = find_seven_zip()

    def list_zipped_file(self, file, password=None):
        args = generate_args(exe=self.exe, password=password, file=file, action='l')
        process = sp.Popen(args, stdout=sp.PIPE)
        output = process.stdout.read()
        process.wait()
        return output.decode('gbk')

    def unzip_zipped_file(self, file, password=None, destination='tmp'):
        args = generate_args(exe=self.exe, password=password, file=file, action='x', destination=destination)
        process = sp.Popen(args, stdout=sp.PIPE)
        output = process.stdout.read()
        process.wait()
        return output
