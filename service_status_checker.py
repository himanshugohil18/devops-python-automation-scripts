import subprocess

service_name = "nginx"

status = subprocess.run(
    ["systemctl", "is-active", service_name],
    capture_output=True,
    text=True
)

if status.stdout.strip() == "active":
    print(f"{service_name} is running")
else:
    print(f"{service_name} is NOT running")