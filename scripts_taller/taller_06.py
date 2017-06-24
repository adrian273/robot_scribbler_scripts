from Myro import *

init('COM3')
rob = getRobot()

def main():
	global rob

frecuencia = [440, 440, 370, 330, 440, 0, 523, 440, 440, 370, 440]
luces = ['left', 'center', 'right', 'left', 'center', 'right',
		'left', 'center', 'right', 'left', 'right']

rob.turnLeft(0.5)
largo = len(frecuencia)
i = 0
while(i < largo):
	frec = frecuencia[i]
	luz = luces[i]
	rob.setLED(luz, 'on')
	rob.beep(0.125, frec)
	rob.setLED(luz, 'off')
	i += 1
	rob.stop()

main()