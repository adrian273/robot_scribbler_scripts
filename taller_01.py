#!/usr/bin/env python
# coding=utf-8

'''
    @description => Taller de robotica
    @name_robot => TUX
'''
import os
from Myro import *

MSG_ERROR = 'Opcion no valida'

# movimientos del robot
class Move(object):

    def __init__(self, speed, second):
        self.speed = speed
        self.second = second

    def move_left(self):
        turnLeft(self.speed, self.second)
        print('Moviendo a la izquierda a la velocidad ' + str(self.speed) + ' con ' + str(self.second) + 's')

    def move_right(self):
        turnRight(self.speed, self.second)
        print('Moviendo a la derecha a la velocidad ' + str(self.speed) + ' con ' + str(self.second) + 's')

    def move_backward(self):
        backward(self.speed, self.second)
        print('Moviendo hacia atras a la velocidad ' + str(self.speed) + ' con ' + str(self.second) + 's')

    def move_forward(self):
        forward(self.speed, self.second)
        print('Moviendo hacia adelante a la velocidad ' + str(self.speed) + ' con ' + str(self.second) + 's')

class Calculation(object):

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        suma = self.n1 + self.n2
        speak('El resultado es ' + str(suma))
        print('la suma es ' + str(suma))

    def resta(self):
        resta = self.n1 - self.n2
        speak('El resultado es ' + str(resta))
        print('la resta es ' + str(resta))

    def multi(self):
        multiplicacion = self.n1 * self.n2
        speak('El resultado es ' + str(multiplicacion))
        print('la multiplicacion es ' + str(multiplicacion))

    def dividir(self):
        division = self.n1 / self.n2
        speak('El resultado es ' + str(division))
        print('la division es ' + str(division))

def photo():
    title = '\n Menu Fotos \n'
    print(title.center(120, '_'))
    count_photo = int(input('Ingrese cantidad de fotos: '))
    for i in range(count_photo):
        wait(1)
        speak('Sacando foto')
        setPictureSize("small")
        img = takePicture("jpeg")
        show(img)
        print(i)
    print('esta es la cantidad de fotos ' + str(count_photo))

def main():
    title = '\n Menu de opciones de TUX \n'
    print(title.center(120, '_'))
    print('1. Sacar fotos \n')
    print('2. Mover \n')
    print('3. Calcular \n')
    print('4. Salir')

def main_move():
    title = '\n Menu movimientos \n'
    print(title.center(120, '_'))
    print('1. Mover a la derecha')
    print('2. Mover a la izquierda')
    print('3. Mover a la atras')
    print('4. Mover a la adelante')
    print('5. Salir')

def main_cals():
    title = '\n Menu de calculos \n'
    print(title.center(120, '_'))
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')

if __name__ == '__main__':
    init('COM3')
    while True:
        main()
        op = int(input('Ingresa tu opcion: '))
        bucle = True
        if op == 1:
            photo()
        elif op == 2:
            main_move()
            while bucle == True:
                op_2 = int(input('Ingresa opcion: '))
                velocity = int(input('Ingrese velocidad: '))
                speed = int(input('Ingrese segundos: '))
                move = Move(velocity, speed)
                if op_2 == 1:
                    move.move_right()
                elif op_2 == 2:
                    move.move_left()
                elif op_2 ==3:
                    move.move_backward()
                elif op_2 == 4:
                    move.move_forward()
                elif op_2 == 5:
                    bucle = False
                else:
                    print("----------------------------> **" + MSG_ERROR)
                main_move()
        elif op == 3:
            main_cals()
            while bucle == True:
                op_3 = int(input('Ingrese opcion: '))
                n1 = int(input('Ingresa numero: '))
                n2 = int(input('Ingresa numero: '))
                cals = Calculation(n1, n2)
                if op_3 == 1:
                    cals.suma()
                elif op_3 == 2:
                    cals.resta()
                elif op_3 == 3:
                    cals.multi()
                elif op_3 == 4:
                    cals.dividir()
                elif op_3 == 5:
                    bucle = False
                main_cals()
        elif op == 4:
            exit()
