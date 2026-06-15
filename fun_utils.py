import os
import datetime
  

def run_command(command):
  print(os.system(command))  

#run_command("du -h")
#run_command("df -h")


def show_date():
  return datetime.datetime.today()

today = show_date()
print(today)