import shutil
import datetime
import os

source = "/etc/nginx"

destination = "/home/ubuntu/nginx_backup"

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

backup_name = os.path.join(destination, f"nginx_{date}")

shutil.make_archive(backup_name, 'gztar', source)

print("Nginx backup completed!")