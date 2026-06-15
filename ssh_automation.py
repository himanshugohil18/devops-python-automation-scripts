import paramiko

hostname = "YOUR_EC2_PUBLIC_IP"
username = "ubuntu"
key_file = "your-key.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=hostname,
    username=username,
    key_filename=key_file
)

stdin, stdout, stderr = ssh.exec_command("df -h")

print(stdout.read().decode())

ssh.close()