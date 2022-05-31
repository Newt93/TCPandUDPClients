import socket

# Useful for buffer overflows etc 

# Change target host to whatever and build upon script
target_host = 'localhost'
target_port = 80

# Create socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect client
client.connect((target_host, target_port))

# Send data
client.send(b'GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n')

# Receive response
response = client.recv(4096)
print(response)
