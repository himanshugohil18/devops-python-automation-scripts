import os
import stat

file_name = input("Enter file name: ")

file_stat = os.stat(file_name)

print("===== FILE PERMISSIONS =====")

print("Readable:", bool(file_stat.st_mode & stat.S_IRUSR))
print("Writable:", bool(file_stat.st_mode & stat.S_IWUSR))
print("Executable:", bool(file_stat.st_mode & stat.S_IXUSR))
