import subprocess

print(
    "\n===== LINUX SECURITY AUDIT ====="
)

# Open Ports
print(
    "\n===== OPEN PORTS ====="
)

open_ports = subprocess.getoutput(
    "ss -tuln"
)

print(open_ports)

# Failed Login Attempts
print(
    "\n===== FAILED LOGIN ATTEMPTS ====="
)

try:
    failed_logins = subprocess.getoutput(
        "grep 'Failed password' /var/log/auth.log | tail -10"
    )

    print(failed_logins)

except:
    print("No failed logins found")

# Sudo Users
print(
    "\n===== SUDO USERS ====="
)

sudo_users = subprocess.getoutput(
    "getent group sudo"
)

print(sudo_users)

# Suspicious Users
print(
    "\n===== USERS WITH SHELL ACCESS ====="
)

users = subprocess.getoutput(
    "awk -F: '$7 ~ /bash|sh/ {print $1}' /etc/passwd"
)

print(users)

print(
    "\n===== AUDIT COMPLETE ====="
)