import schedule
import time
import shutil
import datetime
import os

source = "/home/ubuntu/data"
destination = "/home/ubuntu/backups"

def backup():

    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    backup_name = os.path.join(
        destination,
        f"backup_{timestamp}"
    )

    shutil.make_archive(
        backup_name,
        'gztar',
        source
    )

    print("Backup done!")

schedule.every(1).hours.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)