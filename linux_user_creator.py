import os 

username = input("Enter the username: ")

os.system(f"sudo useradd {username}")

print(f"User {username} created successfully")  