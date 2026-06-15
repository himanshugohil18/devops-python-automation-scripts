import psutil

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent


report = f"""
===== SERVER HEALTH REPORT =====


CPU usage: {cpu}%
RAM usage: {ram}%
DISK usage: {disk}%

"""

with open("server health report.txt", "w") as f:
    f.write(report)

print("report generated successfully!")    