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
    elif losscounter == 1:
        clickMany(4, red.x, red.y)
    elif losscounter == 2:
        clickMany(8, red.x, red.y)
    elif losscounter == 3:
        clickMany(16, red.x, red.y)
    elif losscounter == 4:
        clickMany(32, red.x, red.y)
    elif losscounter == 5:
        clickMany(64, red.x, red.y)
    elif losscounter == 6:
        clickMany(128, red.x, red.y)
    elif losscounter == 7:
        clickMany(256, red.x, red.y)
    elif losscounter == 8:
        clickMany(512, red.x, red.y)
    elif losscounter == 9:
        clickMany(1024, red.x, red.y)
    elif losscounter == 11:
        clickMany(2048, red.x, red.y)
    elif losscounter == 12:
        clickMany(4096, red.x, red.y)
    elif losscounter == 13:
        clickMany(8192, red.x, red.y)
    elif losscounter == 14:
        clickMany(16384, red.x, red.y)
    elif losscounter == 15:
        clickMany(32768, red.x, red.y)



reset = Point(1250, 385)
chipSlider = Point(435, 865)
chip = Point(545, 865)
red = Point(600, 550)
start = Point(1200, 800)

def main():
    while True:
        if keyboard.is_pressed('q'):
            f = open("data.txt","a")
            losscounter = 0
            click(reset.x, reset.y)
            click(chipSlider.x, chipSlider.y)
            click(chip.x, chip.y)
            clicking(losscounter)
            click(start.x, start.y)
            sleep(20)
            while True:
                image = pyautogui.locateOnScreen("poslednavyhra.png",grayscale=True)
                if image is None():
                    losscounter +=1
                    f.write("\n loss, losscounter: " + str(losscounter))
                else:
                    losscounter = 0
                    f.write("\n win, losscounter: " + str(losscounter))
                click(reset.x, reset.y)
                click(chipSlider.x, chipSlider.y)
                click(chip.x, chip.y)
                clicking(losscounter)
                click(start.x, start.y)
                sleep(20)


main()