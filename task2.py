import os 

folders = {}

#d=directories, sd = subdirectories
def directory_list(rootdir):
        for  d, sd in os.walk():
             for files in d:
                files.append(os.path.join(d, files))

for sd in files:
    print(sd)


