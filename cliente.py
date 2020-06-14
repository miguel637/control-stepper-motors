import socket
host = 'host_ip'
port = 8050
# Se importa el módulo

s = socket.socket()

# Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
s.connect((host, port))
print("Conectado al servidor")

while True:
    # Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mens = raw_input("Mensaje desde Cliente a Servidor >> ")
    s.send(mens)
    if (mens == "q"):
        s.close()
        print("Conexión cerrada")
