import shutil
import subprocess as sp
from pathlib import Path
import argparse


def first(action, iterable):
    for i in iterable:
        if action(i):
            return i
    return None


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
        dirs = [r'C:\7z.exe', r'C:\Program Files\7-Zip\7z.exe']
        self.exe = first(lambda d: Path(d).exists(), dirs)
        self.output = []
        self.err = []

    def list_zipped_file(self, file, password=None):
        args = generate_args(exe=self.exe, password=password, file=file, action='l')

        return self.__execute(args)

    def unzip_zipped_file(self, file, password=None, destination='tmp'):
        if password is None:
            args = generate_args(exe=self.exe, file=file, action='x', destination=destination)
        else:
            args = generate_args(exe=self.exe, password=password, file=file, action='x', destination=destination)

        return self.__execute(args)

    def __execute(self, args):
        process = sp.Popen(args, stdin=sp.DEVNULL, stdout=sp.PIPE, stderr=sp.PIPE)
        self.output.append(process.stdout.read())
        self.err.append(process.stderr.read())
        process.wait()
        return process.returncode


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='password', default=None)
    parser.add_argument('-o', dest='out_dir', default='tmp')
    input_args = parser.parse_args()

    if Path(input_args.out_dir).exists():
        shutil.rmtree(input_args.out_dir)

    sz = SevenZip()
    paths = Path('.').glob('*.rar')
    for p in paths:
        rt = sz.unzip_zipped_file(p.name, password=input_args.password, destination=input_args.out_dir)
        if rt == 0:
            print(p.name, 'Ok')
        else:
            print(p.name, 'Fail')
