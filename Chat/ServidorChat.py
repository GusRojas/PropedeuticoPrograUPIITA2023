import socket
import threading

# Configuración del servidor
host = '127.0.0.1'
port = 55555

# Creación del socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Listas para gestionar las conexiones de los clientes y mensajes entrantes
clients = []
usernames = []

# Función para enviar mensajes a todos los clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)

# Función para manejar las conexiones de los clientes
def handle(client):
    while True:
        try:
            # Recepción del mensaje del cliente
            message = client.recv(1024)
            # Envío del mensaje a todos los clientes conectados
            broadcast(message)
        except:
            # Eliminación del cliente y su nombre de usuario
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            break

# Función para recibir conexiones de los clientes y manejarlos
def receive():
    while True:
        # Aceptación de la conexión del cliente
        client, address = server.accept()
        print(f"Conexión establecida con {str(address)}")

        # Solicitud del nombre de usuario del cliente
        client.send("NOMBRE DE USUARIO".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        # Envío de mensaje de bienvenida a todos los clientes conectados
        print(f"{username} se ha unido al chat!")
        broadcast(f"{username} se ha unido al chat!\n".encode('utf-8'))

        # Inicio del hilo para manejar al cliente
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Servidor iniciado...")
receive()
