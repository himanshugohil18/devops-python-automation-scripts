import psutil

disk = psutil.disk_usage('/').percent

threshold = 80

if disk > threshold:
    print(f"WARNING! Disk usage: {disk}%")
else:
    print("Disk usage normal")