import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from AtomImg import recursos

import socket

import pygame
import time
from threading import Thread

#Declaro la ip y el puerto que vamos a usar
host = '192.168.1.12'
port = 8083

done=False
joysticks = []
global reconectar
global reconectando


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class interfaceCliente_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("AtomInterface.ui",self)
        self.show()
        self.EstadoConectado.setVisible(0)
        self.BuscandoConexion.setVisible(0)
        self.giroDerecha.setVisible(0)
        self.giroIzquierda.setVisible(0)
        self.press_a.setVisible(0)
        self.press_b.setVisible(0)
        self.press_x.setVisible(0)
        self.press_y.setVisible(0)

        self.RB.setVisible(0)
        self.LB.setVisible(0)
        self.LT.setVisible(0)
        self.RT.setVisible(0)

        self.up.setVisible(0)
        self.down.setVisible(0)
        self.left.setVisible(0)
        self.right.setVisible(0)

        self.cuadritos.setVisible(0)
        self.lineas.setVisible(0)

        self.press_leftJ.setVisible(0)
        self.press_rightJ.setVisible(0)

        self.downJ.setVisible(0)
        self.upJ.setVisible(0)
        self.leftJ.setVisible(0)
        self.rightJ.setVisible(0)

        self.upJ_2.setVisible(0)
        self.downJ_2.setVisible(0)
        self.leftJ_2.setVisible(0)
        self.rightJ_2.setVisible(0)

        #faltan gatillos, gatillos secundarios, botones de menu

        self.Conectar.clicked.connect(self.conectarSistema)
        self.desconectar.clicked.connect(self.deconectarSistema)

    def comandosControl(self):
        pygame.init()
        pygame.joystick.init()
        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[-1].init()

    def refreshJoystickStatus(self):

        global done
        JOY_THRESHOLD = 0.5   #Palancas
        JOY_THRESHOLD2 = 0.5  #Gatillos

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        while done==False:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done=True

                if event.type == pygame.JOYBUTTONDOWN:

                    click = event.button

                    if click == 0:
                        print('button_A')
                        while(click == 0):
                           self.press_a.setVisible(1)
                           s.send('l'.encode(encoding='utf_8'))
                           click = pygame.event.get()


                    if click == 1:
                        self.press_b.setVisible(1)
                        s.send('j'.encode(encoding='utf_8'))
                        print('button_B')

                    if click == 3:
                        self.press_y.setVisible(1)
                        s.send('k'.encode(encoding='utf_8'))
                        print('button_Y')

                    if click == 2:
                        self.press_x.setVisible(1)
                        s.send('p'.encode(encoding='utf_8'))
                        print('button_x')

                    if click == 6:
                        self.cuadritos.setVisible(1)
                        s.send('c'.encode(encoding='utf_8'))
                        print('cuadritos')

                    if click == 7:
                        self.lineas.setVisible(1)
                        s.send('n'.encode(encoding='utf_8'))
                        print('lineas')

                    if click == 4:
                        self.LB.setVisible(1)
                        s.send('i'.encode(encoding='utf_8'))
                        print('LB')

                    if click == 5:
                        self.RB.setVisible(1)
                        s.send('e'.encode(encoding='utf_8'))
                        print('RB')

                    if click == 8:
                        self.press_leftJ.setVisible(1)
                        print('J_left')

                    if click == 9:
                        self.press_rightJ.setVisible(1)
                        print('R_left')



                else:
                    self.press_a.setVisible(0)
                    self.press_b.setVisible(0)
                    self.press_y.setVisible(0)
                    self.press_x.setVisible(0)

                    self.press_leftJ.setVisible(0)
                    self.press_rightJ.setVisible(0)

                    self.RB.setVisible(0)
                    self.LB.setVisible(0)

                    self.cuadritos.setVisible(0)
                    self.lineas.setVisible(0)

                if event.type == pygame.JOYHATMOTION:
                    if joysticks[-1].get_hat(0) == (0, 1):
                        self.up.setVisible(1)
                        s.send('v'.encode(encoding='utf_8'))
                        print("up")
                    if joysticks[-1].get_hat(0) == (0, -1):
                        self.down.setVisible(1)
                        s.send('b'.encode(encoding='utf_8'))
                        print("down")
                    if joysticks[-1].get_hat(0) == (-1, 0):
                        self.left.setVisible(1)
                        print("left")
                    if joysticks[-1].get_hat(0) == (1, 0):
                        self.right.setVisible(1)
                        s.send('g'.encode(encoding='utf_8'))
                        print("right")
                    if joysticks[-1].get_hat(0) == (0, 0):
                        self.up.setVisible(0)
                        self.down.setVisible(0)
                        self.left.setVisible(0)
                        self.right.setVisible(0)




            axisY=joystick.get_axis(1)

            if(axisY > JOY_THRESHOLD):
                s.send('s'.encode(encoding='utf_8'))
                self.downJ.setVisible(1)
                print('S-J1_down')
                while(axisY> JOY_THRESHOLD):
                    pygame.event.get()
                    axisY=joystick.get_axis(1)
                self.downJ.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            elif(axisY < -JOY_THRESHOLD):
                s.send('w'.encode(encoding='utf_8'))
                self.upJ.setVisible(1)
                print('W-J1_up')
                while(axisY < -JOY_THRESHOLD):
                    pygame.event.get()
                    axisY=joystick.get_axis(1)
                self.upJ.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            axisY2 = joystick.get_axis(3)

            if (axisY2 > JOY_THRESHOLD2):
                s.send('u'.encode(encoding='utf_8'))
                self.downJ_2.setVisible(1)
                print('A-J2_down')
                while(axisY2 > JOY_THRESHOLD2):
                    pygame.event.get()
                    axisY2 = joystick.get_axis(3)
                self.downJ_2.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            elif (axisY2 < -JOY_THRESHOLD2):
                s.send('o'.encode(encoding='utf_8'))
                self.upJ_2.setVisible(1)
                print('D-J2_up')
                while (axisY2 < -JOY_THRESHOLD2):
                    pygame.event.get()
                    axisY2 = joystick.get_axis(3)
                self.upJ_2.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            Gatillos = joystick.get_axis(2)

            if (Gatillos > JOY_THRESHOLD2):
                s.send('y'.encode(encoding='utf_8'))
                self.LT.setVisible(1)
                print('A-LT')
                while (Gatillos > JOY_THRESHOLD2):
                    pygame.event.get()
                    Gatillos = joystick.get_axis(2)
                self.LT.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            elif (Gatillos < -JOY_THRESHOLD2):
                s.send('r'.encode(encoding='utf_8'))
                self.RT.setVisible(1)
                print('D-RT')
                while (Gatillos < -JOY_THRESHOLD2):
                    pygame.event.get()
                    Gatillos = joystick.get_axis(2)
                self.RT.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            axisX2 = joystick.get_axis(4)

            if (axisX2 > JOY_THRESHOLD):
                s.send('z'.encode(encoding='utf_8'))
                self.rightJ_2.setVisible(1)
                print('D-J2_Right')
                while (axisX2 > JOY_THRESHOLD2):
                    pygame.event.get()
                    axisX2= joystick.get_axis(4)
                self.rightJ_2.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            elif (axisX2 < -JOY_THRESHOLD2):
                s.send('t'.encode(encoding='utf_8'))
                self.leftJ_2.setVisible(1)
                print('A-J2_Left')
                while (axisX2 < -JOY_THRESHOLD2):
                    pygame.event.get()
                    axisX2 = joystick.get_axis(4)
                self.leftJ_2.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            axisX = joystick.get_axis(0)

            if (axisX > JOY_THRESHOLD):
                s.send('d'.encode(encoding='utf_8'))
                self.giroDerecha.setVisible(1)
                self.Adelante.setVisible(0)
                self.rightJ.setVisible(1)
                print('X-J_Right')
                while (axisX > JOY_THRESHOLD2):
                    pygame.event.get()
                    axisX = joystick.get_axis(0)
                self.giroDerecha.setVisible(0)
                self.Adelante.setVisible(1)
                self.rightJ.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

            elif (axisX < -JOY_THRESHOLD2):
                s.send('a'.encode(encoding='utf_8'))
                self.Adelante.setVisible(0)
                self.giroIzquierda.setVisible(1)
                self.leftJ.setVisible(1)
                print('Z-J_Left')
                while (axisX < -JOY_THRESHOLD2):
                    pygame.event.get()
                    axisX = joystick.get_axis(0)
                self.Adelante.setVisible(1)
                self.giroIzquierda.setVisible(0)
                self.leftJ.setVisible(0)
                print('Stop')
                s.send('q'.encode(encoding='utf_8'))

    pygame.quit()


    def conectarSistema(self):

        print("Conectado...")
        self.BuscandoConexion.setVisible(1)
        self.EstadoDesconectado.setVisible(0)
        s.connect((host, port))
        print("Conectado al servidor correctamente")
        self.EstadoConectado.setVisible(1)
        self.BuscandoConexion.setVisible(0)
        iniciarControl()

    def deconectarSistema(self):
        self.BuscandoConexion.setVisible(1)
        self.EstadoConectado.setVisible(0)
        self.EstadoDesconectado.setVisible(0)
        print("desconectado")
        s.close()
        sys.exit(app.exec_())







def main():
    GUI.comandosControl()
    GUI.show()
    sys.exit(app.exec_())

def iniciarControl():
    GUI.refreshJoystickStatus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = interfaceCliente_GUI()
    main()
