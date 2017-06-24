from Graphics import *
from Myro import *

init('COM3')

getRobot()

win = Window('Test', 500, 240)
win.Show()
while(win.Visible):
	ir_left = getIR('left')
	ir_right = getIR('right')
	
	distance_left = getDistance('left')
	distance_right = getDistance('right')
	text = Text(Point(100, 50), str(distance_left))
	text.draw(win)
	#print('IR: {} {} -- Distancia {} {} '.format(ir_left,ir_right,distance_left,distance_right))
