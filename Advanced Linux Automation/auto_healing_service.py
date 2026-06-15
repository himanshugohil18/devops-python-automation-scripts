import subprocess
import os
import time

service = "nginx"

while True:
    status = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )

    if status.stdout.strip() != "active":
        print("Service down! Restarting...")

        os.system(
            f"sudo systemctl restart {service}"
        )

    else:
        print("Service healthy")

    time.sleep(60)