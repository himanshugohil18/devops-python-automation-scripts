import os

file_name = input("Enter file name: ")

permission = input("Enter permission (example 755): ")

os.system(f"chmod {permission} {file_name}")

print("Permission changed successfully!")