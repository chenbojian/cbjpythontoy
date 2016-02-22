import os
import zipfile
import shutil


def zip_dir(my_path, dir_name):
    f = zipfile.ZipFile(dir_name + '.zip', 'w')
    old_path = os.getcwd()
    os.chdir(my_path)
    for dir_path, dir_names, file_names in os.walk('.'):
        for filename in file_names:
            f.write(os.path.join(dir_path, filename))
    os.chdir(old_path)
    f.close()


def rename_comic():
    count = 0
    for dirAndFile in os.listdir('.'):
        if os.path.isdir(dirAndFile):
            shutil.move(os.path.join(dirAndFile, dirAndFile), os.path.join(dirAndFile, 'fate' + str(count)))
            shutil.move(dirAndFile, 'fate' + str(count))
            count += 1


def zip_comic():
    for dirAndFile in os.listdir('.'):
        if os.path.isdir(dirAndFile):
            dir_name = dirAndFile
            my_path = os.path.join('.', dir_name)
            zip_dir(my_path, dir_name)


rename_comic()
zip_comic()
