import shutil
import datetime
import os
        
def backup_files(source,destination):
    today = datetime.datetime.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive (backup_file_name,'gztar',source)

source = "/mnt/c/Users/Himanshu/Downloads/Python - Practice"
destination = "/mnt/c/Users/Himanshu/Downloads/Python - Practice/backups"

backup_files(source,destination)
