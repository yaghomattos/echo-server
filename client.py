import socket
import sys

HOST = 'localhost'
PORT = 4444

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print('To quit use "quit"')

message = "echo Connected"

while True:
    try:
        client_socket.send(bytes(message, 'utf8'))
        response = client_socket.recv(1024)
        response = response.decode()
        print('Received from server:', response)
        if message == 'quit':
            break
        message = input()

    except KeyboardInterrupt:
        client_socket.send(bytes('exit', 'utf8'))
        print('Connection Iterrupt')
        sys.exit()


print('Connection closed')
client_socket.close()
