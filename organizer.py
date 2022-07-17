import os

DESTINATION_DIRECTORY_LIST = set()
FILE_TYPES = {}
CURRENT_DIRECTORY_PATH = os.getcwd()

curr_dir = os.scandir()
files_count = 0

for entry in curr_dir:
    if entry.is_file() and entry.name!='organizer.py':
        file_name = entry.name
        file_type = file_name[len(file_name)-file_name[::-1].find('.'):]
        destination_path = f"{CURRENT_DIRECTORY_PATH}/{file_type}_files"
        if(file_type not in FILE_TYPES):
            os.mkdir(destination_path)
            FILE_TYPES[file_type] = 1
            DESTINATION_DIRECTORY_LIST.add(destination_path)
        else:
            FILE_TYPES[file_type] += 1
        os.rename(f"{CURRENT_DIRECTORY_PATH}/{file_name}",f"{destination_path}/{file_name}")
        files_count+=1
else:
    if(files_count>0):
        print(f"Total Files Count : {files_count}")
        print("File Types Present:",end=" ")
        print(*FILE_TYPES,sep="|")
        print("Individual File Counts :",FILE_TYPES)
    else:
        print("No files found in current directory")

curr_dir.close()