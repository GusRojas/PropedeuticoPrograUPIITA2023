# Cliente
import socket

host = '127.0.0.1'
port = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

##message = 'Hola, servidor!'
print('Escribe tu mensaje: ')
message = input()
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print('Mensaje recibido del servidor: {}'.format(data.decode()))

client_socket.close()