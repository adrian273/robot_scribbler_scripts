# -*- coding: utf-8 -*-
from Myro import *

init("COM3")

ELLIOT = getRobot()

senses()
while True:
    left, right = ELLIOT.getLine()
    print('left: {} -> right: {}'.format(left, right))
    if left == 1 and right == 1:
        motors(-0.1, -0.1)
    elif left == 1 and right == 0:
        motors(-0.1, 1.0)
    elif left == 0 and right == 1:
        motors(1.0, -1.0)
    elif left == 0 and right == 0:
        motors(0.1, 0.273)