import time
from Myro import *
init('COM3')
getRobot()

energy = 1
duration = 0.5

init_test = time.time()
now = time.time()

while((now - init_test) < 10):
	turnLeft(energy, duration)
	turnRight(energy, duration)
	now = time.time()

stop()