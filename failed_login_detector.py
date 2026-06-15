log_file = "/var/log/auth.log"

print("===== FAILED LOGIN ATTEMPTS =====")

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            print(line.strip())