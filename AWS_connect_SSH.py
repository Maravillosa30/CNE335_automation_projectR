import paramiko

host = '35.160.182.172'
port = 22
username = 'ec2-user'
private_key_path = r"C:\Users\esono\OneDrive\Escritorio\F_ll023.pem"

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure, see comments below)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Load your private key
private_key = paramiko.RSAKey(filename=private_key_path)

# Connect to the server
client.connect(host, port, username, pkey=private_key)

# Run the update commands
commands = [
    'sudo yum update  -y',
    'sudo yum upgrade -y'
]

for command in commands:
    print(f"Running command: {command}")
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode('utf-8'))
    print(stderr.read().decode('utf-8'))

# Disconnect from the server
client.close()
