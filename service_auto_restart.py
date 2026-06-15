import subprocess
import os

service_name = "nginx"

status = subprocess.run(
    ["systemctl", "is-active", service_name],
    capture_output=True,
    text=True
)

if status.stdout.strip() != "active":
    print(f"{service_name} is down...")
    print("Restarting service...")

    os.system(f"sudo systemctl restart {service_name}")

    print("Service restarted successfully")
else:
    print(f"{service_name} is already running")