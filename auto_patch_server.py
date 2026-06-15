import os

print("Updating packages...")

os.system("sudo apt update")
os.system("sudo apt upgrade -y")

print("Server updated successfully!")