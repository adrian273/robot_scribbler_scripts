from Myro import *

init("COM3")
rob = getRobot()

def main():
    global rob
    rob.setPicSize('large')
    foto = rob.takePicture('jpeg')
    ancho = foto.width
    alto =  foto.height
    print("Ancho de la foto {}, Alto de la foto {}".format(ancho, alto))
    y = 10
    x = 0
    while(x < ancho):
        pixel = foto.getPixel(x, y)
        pixel.setRGB(255, 0, 0)
        x += 1
        show(foto)
        savePicture(foto, 'img.jpg')
main()