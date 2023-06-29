import socket
import threading

# Configuración del cliente
host = '127.0.0.1'
port = 55555

# Nombre de usuario del cliente
username = input('Ingrese su nombre de usuario: ')

# Creación del socket del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Función para recibir mensajes del servidor
def receive():
    while True:
        try:
            # Recepción del mensaje del servidor
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                # Envío del nombre de usuario al servidor
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            # Cierre del socket del cliente en caso de error
            print('Ha ocurrido un error al recibir el mensaje.')
            client.close()
            break

# Función para enviar mensajes al servidor
def write():
    while True:
        message = f'{username}: {input("")}'
        # Envío del mensaje al servidor
        client.send(message.encode('utf-8'))

# Configuración de los hilos para recibir y enviar mensajes
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
