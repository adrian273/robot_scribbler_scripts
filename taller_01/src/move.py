# -*- coding: utf-8 -*-
from Myro import *


class Move(object):

    def __init__(self, speed, second):
        self.speed = speed
        self.second = second

    def right_move(self):
        return turnRight(self.speed, self.second)

    def left_move(self):
        return turnLeft(self.speed, self.second)

    def forward_move(self):
        return forward(self.speed, self.second)

    def backward_move(self):
        return backward(self.speed, self.second)