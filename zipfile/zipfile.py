# -*- coding:utf-8 -*-
import os
import zipfile
import shutil
def zipDir(mypath,dirname):
    f = zipfile.ZipFile(dirname+'.zip', 'w')
    oldpath = os.getcwd()
    os.chdir(mypath)
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            f.write(os.path.join(dirpath,filename))
    os.chdir(oldpath)
    f.close()

def renameComic():
    count = 0
    for dirAndFile in os.listdir('.'):
       if os.path.isdir(dirAndFile):
           shutil.move(os.path.join(dirAndFile,dirAndFile),os.path.join(dirAndFile,'fate'+str(count)))
           shutil.move(dirAndFile,'fate'+str(count))
           count += 1
def zipComic():
    for dirAndFile in os.listdir('.'):
       if os.path.isdir(dirAndFile):
           dirname = dirAndFile
           mypath = os.path.join('.',dirname)
           zipDir(mypath,dirname)

renameComic()
zipComic()
