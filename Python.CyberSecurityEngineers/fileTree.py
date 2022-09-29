from os import listdir,scandir,path
from datetime import datetime, timezone

rootDirectory = "/var"

dirList = listdir(rootDirectory)
dirList.sort()

for dir in dirList:
    print("-- folderName: {}\n".format(dir))
    try:
        # got 'No file on directory' error without adding '/' beetween rootDirectory and next folder
        for path in scandir(rootDirectory + "/" + dir): 
            if path.is_file():
               file_name = path.name
               file_size = str(path.stat().st_size)
               file_creation_date = int(path.stat().st_ctime)
               print("----- fileName: {} fileSize: {} fileCreationDate: {}".format(file_name,file_size,datetime.fromtimestamp(file_creation_date,tz=timezone.utc)))
    except PermissionError:
        print("No permissions. Skip this folder")