import socket
import psutil
import platform
import csv
import subprocess

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

ram = round(
    psutil.virtual_memory().total / (1024**3),
    2
)

disk = round(
    psutil.disk_usage('/').total / (1024**3),
    2
)

uptime = subprocess.getoutput(
    "uptime -p"
)

file_name = "server_inventory.csv"

with open(file_name, "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "Hostname",
        "IP Address",
        "RAM (GB)",
        "Disk (GB)",
        "Uptime"
    ])

    writer.writerow([
        hostname,
        ip_address,
        ram,
        disk,
        uptime
    ])

print(
    f"Inventory report saved: {file_name}"
)