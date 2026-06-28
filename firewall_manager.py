import os

print("Opening ports...")

os.system("sudo ufw allow 22")
os.system("sudo ufw allow 80")
os.system("sudo ufw allow 443")

os.system("sudo ufw enable")

print("Firewall configured successfully!")
