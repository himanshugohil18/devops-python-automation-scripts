import os

days = 7

command = f"find /var/log -type f -mtime +{days} -delete"

os.system(command)

print(f"Logs older than {days} days deleted")
