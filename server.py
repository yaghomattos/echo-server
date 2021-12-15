import socket
import threading
import sys

if __name__ == '__main__':

    HOST = ''
    PORT = 4444

    class connect(threading.Thread):

        def __init__(self, name, delay):
            threading.Thread.__init__(self)
            self.threadedClient_socket = client_socket
            print('\nConnecting to:', address)

        def run(self):
            finished = ''
            while True:
                message = self.threadedClient_socket.recv(1024)
                message = message.decode()

                if message.startswith('echo '):
                    message = message.split('echo ', 1)
                    print('Client', address, message[1])
                    self.threadedClient_socket.send(bytes(message[1], 'utf-8'))
                elif message == 'quit' or message == 'exit':
                    finished = message
                    print('Client', address, message)
                    self.threadedClient_socket.send(
                        bytes('Quiting...', 'utf-8'))
                    break
                else:
                    self.threadedClient_socket.send(
                        bytes('ERROR! Use the echo command + message.', 'utf-8'))
                    print('Client', address, 'ERROR! Unknown command.')

            print('Client', address, 'connection closed')
            self.threadedClient_socket.send(bytes('Disconnecting...', 'utf-8'))
            self.threadedClient_socket.close()
            if finished == 'exit':
                server_socket.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    print('\nServer init in port:', PORT)

    server_socket.listen()

    while True:
        try:
            client_socket, address = server_socket.accept()
            thread = connect(client_socket, address)
            thread.start()
            print('Active clients:', threading.active_count() - 1)
            print('Messages:')
        except Exception:
            print('Connetion interrupt! Ending with the last connection.')
            sys.exit()
