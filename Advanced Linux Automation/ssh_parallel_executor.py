import paramiko
from concurrent.futures import ThreadPoolExecutor

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

command = "df -h"

def execute(server):

    try:
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        ssh.connect(
            hostname=server["host"],
            username=server["username"],
            key_filename=server["key"]
        )

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()

        print(
            f"\n===== {server['host']} ====="
        )

        print(output)

        ssh.close()

    except Exception as error:
        print(
            f"Failed on {server['host']}"
        )
        print(error)

with ThreadPoolExecutor(
    max_workers=10
) as executor:

    executor.map(execute, servers)