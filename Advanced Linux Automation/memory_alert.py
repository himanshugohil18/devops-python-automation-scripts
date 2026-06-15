import psutil

memory = psutil.virtual_memory().percent

if memory > 80:
    print("RAM usage too high!")
else:
    print("RAM usage normal")
    