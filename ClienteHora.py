import socket

# dirección IP y puerto del servidor
server_address = ('127.0.0.1', 8888)

# creación del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conexión al servidor
client_socket.connect(server_address)

# envío de la solicitud de hora actual
client_socket.sendall(b'solicitar hora')

# recepción de la hora actual del servidor
hora_actual = client_socket.recv(1024)

# cierre del socket
client_socket.close()

print('La hora actual es:', hora_actual.decode())