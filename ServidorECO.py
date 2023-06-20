# Servidor
import socket

host = '127.0.0.1'
port = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('Servidor escuchando en {}:{}'.format(host, port))

while True:
    conn, addr = server_socket.accept()
    print('Conexión entrante desde {}:{}'.format(addr[0], addr[1]))
    data = conn.recv(1024)
    conn.sendall(data)
    conn.close()