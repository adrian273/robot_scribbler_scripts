# -*- coding: utf-8 -*-

from Myro import *
from src import Main
from src import Move


def initialize():
    while True:
        title = '| Menu Robot Scripbller S2 | '
        print(title)
        # opciones del menu principal
        for primary_op in MAIN.primary_main():
            print(primary_op)
        option = int(input('Ingrese su opcion : '))
        if option == 1:
            speed = int(input('Ingrese velocidad'))
            second = int(input('Ingrese tiempo'))
            MOVE = Move(speed, second)
            title_move = '| Menu de movimiento |'
            print(title_move)
            # menu de opciones de movimiento
            for m in MAIN.move_main():
                print(m)
            op = int(input('Ingrese su opcion: '))
            if op == 1:
                MOVE.right_move()
            elif op == 2:
                MOVE.left_move()
            elif op == 3:
                MOVE.backward_move()
            elif op == 4:
                MOVE.forward_move()

if __name__ == '__main__':
    init('COM3')
    MAIN = Main()
    initialize()