import os
import shutil
import itertools as it
import subprocess as sp
from pathlib import Path
import argparse


class EnterDir(object):
    def __init__(self, dir):
        self.dir = dir
        self.current_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_dir)


def first(action, iterable):
    for i in iterable:
        if action(i):
            return i
    return None


class SevenZip(object):
    def __init__(self):
        dirs = [r'C:\7z.exe', r'C:\Program Files\7-Zip\7z.exe']
        self.exe = first(lambda d: Path(d).exists(), dirs)
        self.output = []
        self.err = []

    def list(self, file, password=None):
        if password is None:
            args = [self.exe, 'l', file]
        else:
            args = [self.exe, 'l', '-p' + password, file]

        return self.__execute(args)

    def unzip(self, file, password=None, destination='tmp'):
        if password is None:
            args = [self.exe, 'x', '-o' + destination, file]
        else:
            args = [self.exe, 'x', '-p' + password, '-o' + destination, file]

        return self.__execute(args)

    def zip(self, dir):
        args = [self.exe, 'a', '-tzip', dir + '.zip', dir]
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

    paths = it.chain(Path('.').glob('*.rar'), Path('.').glob('*.zip'))
    for p in paths:
        rt = SevenZip().unzip(p.name, password=input_args.password, destination=input_args.out_dir)
        if rt == 0:
            print(p.name, 'UNZIP---Ok')
        else:
            print(p.name, 'UNZIP---Fail')

    with EnterDir(input_args.out_dir):
        for d in Path('.').glob('*'):
            rt = SevenZip().zip(d.name)
            if rt == 0:
                print(d.name, 'ZIP---Ok')
            else:
                print(d.name, 'ZIP---Fail')
