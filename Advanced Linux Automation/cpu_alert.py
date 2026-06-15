import psutil

cpu = psutil.cpu_percent(interval=1)

threshold = 80

if cpu > threshold:
    print(f"ALERT! CPU usage is {cpu}%")
else:
    print("CPU is normal")