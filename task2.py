import os

folders = {}

#d=directories, sd = subdirectories
def directory_list(rootdir):
    for  d, sd in os.walk():
        for folders in d:
            folders.append(os.path.join(d, folders)

for sd in folders:
    print(sd)

directory_list_list(./)


