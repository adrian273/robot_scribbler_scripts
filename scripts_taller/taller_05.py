from Myro import *
init('COM3')
energy = 10
second = 10
while True:
    backward(energy, second)
    
    left_ir = getIR('left')
    right_ir = getIR('right')
    #  luces
    get_center = getLight('center')
    get_left = getLight('left')
    get_right = getLight('right')
    
    #  distancia
    get_distance_left = getDistance('left')
    get_distance_right = getDistance('right')
    
    #obtaculos
    get_obstacle_left = getObstacle(0)
    get_obstacle_right = getObstacle(2)
    get_obstacle_center = getObstacle(1)
    
    #get_bright_left = getBright(0)
    
    if get_obstacle_left < 100:
        forward(10,1)
        turnRight(5,2)
        print('Obstaculo encontrado left {}'.format(get_obstacle_left))
    elif get_obstacle_right < 100:
        #turnLeft(10,2)
        forward(10,1)
        print('Obstaculo encontrado right {}'.format(get_obstacle_right))
    elif get_obstacle_center < 100:
        forward(10,1)
        print('Obstaculo encontrado center {}'.format(get_obstacle_center))
        
    if get_distance_left < 80:
        turnRight(10,2)
        print('doblando a la derecha')
    elif get_distance_right < 80:
        print('doblando a la izquierda')
        turnLeft(10,2)
        
    print('distance_left: {}- distance_right {}'.format(get_distance_left,get_distance_right))
    print('get_left {} - get_right {} get_center {}'.format(get_left,get_right, get_center))
    print('get_left_ir {} - right_ir {}'.format(left_ir,right_ir))
    print('-----------------')
    print('Nivel de bateria: ' + str(getBattery()))
    #print("bright_left: {}".format(get_bright_left))