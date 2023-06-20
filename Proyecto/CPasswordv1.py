import socket

HOST = '127.0.0.1'  # dirección IP del servidor
PORT = 65432  # número de puerto

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

requisitos = input('Ingrese los requisitos de la contraseña (longitud,mayusculas,minusculas,numeros,caracteres especiales): ')
s.sendall(requisitos.encode())

with open('contrasenas.txt', 'w') as f:
    while True:
        data = s.recv(1024)
        s.close()
        #if not data:
        #    break
        #s.close()            
        f.write(data.decode() + '\n')
        print(data.decode())

        #s.close()

