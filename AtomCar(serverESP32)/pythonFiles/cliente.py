from tkinter import *
import socket

print("Conectado al servidor")

#Variables
host = '192.168.1.17'
port = 8266

#Creación de un objeto socket (lado cliente)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def key_pressed(c):
    print("key pressed", c.char)
    est=c.char
    if(est=='p'):
        s.connect((host, port))
        reconectar
    else:
        s.send(c.char.encode(encoding='utf_8'))


def key_released(c):
    print("key released", c.char)
    s.send('q'.encode(encoding='utf_8'))

def reconectar(c):
    s.close(not self)
    print("reconectando")
    s.connect((host, port))
    print("reconectado correctamente")

root = Tk()
root.title('Controlador')


frame = Frame(root)

lbl_titulo = Label(frame, text='cojtrolador Robot')
lbl_titulo.grid(row=0, column=0, pady=10,padx=10)

frame.bind('<KeyPress>', key_pressed)
frame.bind('<KeyRelease>', key_released)

#Conexión con el servidor
s.connect((host, port))
print("Conectado al servidor")

frame.pack()
frame.focus_set()

root.mainloop()

