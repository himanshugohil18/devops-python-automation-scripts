import time

log_file = "/var/log/syslog"

keywords = ["error", "failed"]

with open(log_file, "r") as file:
    file.seek(0, 2)

    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        for word in keywords:
            if word in line.lower():
                print(
                    f"ALERT FOUND: {line.strip()}"
                )