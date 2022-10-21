import os
import shutil
import send2trash


def selective_copy(dest, src=os.getcwd(), ext='.jpg'):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for foldername,  subfoldernames, filenames in os.walk(src):
        for filename in filenames:
            if filename.endswith(ext):
                shutil.copy(os.path.join(foldername, filename), dest)


def deleting_unneeded(dir):
    big_size = 100 * 1024 * 1024
    for foldername,  subfoldernames, filenames in os.walk(dir):
        for filename in filenames:
            file = os.path.join(foldername, filename)
            if os.path.getsize(file) > big_size:
                send2trash.send2trash(file)


def filling_gaps(dir=os.getcwd()):
    files = []
    for file in os.listdir(dir):
        if file.startswith('spam'):
            files.append(os.path.join(dir, file))
    files.sort()
    for i in range(len(files)):
        shutil.move(files[i], os.path.join(
            dir, 'spam%s.txt' % str(i+1).rjust(3, '0')))


def empty_number(numbers=10, empty=[]):
    for number in range(1, numbers+1):
        if number not in empty:
            with open(dir + '/spam%s.txt' % str(number).rjust(3, '0'), 'w') as f:
                pass
