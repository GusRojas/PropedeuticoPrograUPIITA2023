import socket
import secrets
import string

def generar_contrasena(requisitos):
    longitud, mayusculas, minusculas, numeros, caracteres_especiales = requisitos
    alfabeto = ''
    if mayusculas == 'True':
        alfabeto += string.ascii_uppercase
    if minusculas == 'True':
        alfabeto += string.ascii_lowercase
    if numeros == 'True':
        alfabeto += string.digits
    if caracteres_especiales == 'True':
        alfabeto += string.punctuation
    contrasena = ''.join(secrets.choice(alfabeto) for i in range(int(longitud)))
    return contrasena

HOST = '127.0.0.1'  # dirección IP del servidor
PORT = 65432  # número de puerto

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conexiones = []
    #while True:
   #     conn, addr = s.accept()
    #    conexiones.append(conn)
    #    print('Conexión establecida por', addr)

    while True:
        conn, addr = s.accept()
        with conn:
            print('Conexión establecida por', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                requisitos = data.decode().split(',')
                contrasena = generar_contrasena(requisitos)
                conn.sendall(contrasena.encode())
                #conn.close()
            

