import pyautogui
import keyboard
from time import sleep

pyautogui.PAUSE = 0.001

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def click(x, y):
    pyautogui.click(x, y)

def clickMany(clicks, x, y):
    i = 0
    while (i < clicks):
        click(x,y)
        i+=1

def clicking(losscounter):
    if losscounter == 0:
        clickMany(2, red.x, red.y)
    else
        clickMany(pow(2,losscounter+1), red.x, red.y)
        
def program(reset, chipSlider, chip, red, start):
       click(reset.x, reset.y)
       click(chipSlider.x, chipSlider.y)
       click(chip.x, chip.y)
       clicking(losscounter)
       click(start.x, start.y)
       sleep(20)

reset = Point(1250, 385)
chipSlider = Point(435, 865)
chip = Point(545, 865)
red = Point(600, 550)
start = Point(1200, 800)

def main():
    while True:
        if keyboard.is_pressed('q'):
            losscounter = 0
            program(reset, chipSlider, chip, red, start)
            while True:
                image = pyautogui.locateOnScreen("poslednavyhra.png",grayscale=True)
                if image is None():
                    losscounter +=1
                else:
                    losscounter = 0
                program(reset, chipSlider, chip, red, start)
                sleep(20)


main()
