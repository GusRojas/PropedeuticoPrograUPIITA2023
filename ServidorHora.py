import socket
import datetime

# dirección IP y puerto del servidor
server_address = ('127.0.0.1', 8888)

# creación del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enlace del socket a la dirección y puerto del servidor
server_socket.bind(server_address)

# escucha de conexiones entrantes
server_socket.listen(1)

print('Servidor iniciado en', server_address)

while True:
    # aceptación de la conexión entrante
    client_socket, client_address = server_socket.accept()
    print('Conexión entrante desde', client_address)

    # recepción de la solicitud del cliente
    solicitud = client_socket.recv(1024)

    if solicitud == b'solicitar hora':
        # obtención de la hora actual
        hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Hora actual:', hora_actual)

        # envío de la hora actual al cliente
        client_socket.sendall(hora_actual.encode())

    # cierre del socket del cliente
    client_socket.close()