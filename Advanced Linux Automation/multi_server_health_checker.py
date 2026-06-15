import paramiko

servers = [
    {
        "host": "SERVER_IP_1",
        "username": "ubuntu",
        "key": "key.pem"
    },
    {
        "host": "SERVER_IP_2",
        "username": "ubuntu",
        "key": "key.pem"
    }
]

command = "top -bn1 | head -5 && free -h && df -h"

for server in servers:
    print(f"\nChecking {server['host']}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=server["host"],
        username=server["username"],
        key_filename=server["key"]
    )

    stdin, stdout, stderr = ssh.exec_command(command)

    print(stdout.read().decode())

    ssh.close()