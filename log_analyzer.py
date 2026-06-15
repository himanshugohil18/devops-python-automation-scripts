log_file = "/var/log/syslog"

keywords = ["error","failed" , "warning"]

print("===== LOG ANALYZER =====")

with open(log_file, "r") as file:
    for line in file:
        for keyword in keywords:
            if keyword in line.lower():
                print(line.strip())