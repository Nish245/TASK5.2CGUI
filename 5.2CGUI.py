from tkinter import *
import tkinter.font
from gpiozero import PWMLED
import RPi.GPIO
import math

RPi.GPIO.setmode(RPi.GPIO.BCM)

## GPIO pin declarations/Initialize PWM LED ##
ledBlue = PWMLED(17)
ledRed = PWMLED(18)
ledGreen = PWMLED(27)

## GUI DEFINITION ##
win = Tk()
win.title("LED Intensity Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

### EVENT FUNCTIONS ###

# BLUE SLIDER #
def updateRed(value):
    blueCycle = math.sqrt(float(value) / 100)
    ledRed.value = blueCycle

# RED SLIDER #
def updateBlue(value):
    redCycle = math.sqrt(float(value) / 100)
    ledBlue.value = redCycle

# GREEN SLIDER #
def updateGreen(value):
    greenCycle = math.sqrt(float(value) / 100)
    ledGreen.value = greenCycle

# Function to exit and cleanup GPIO
def exitToggle():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###

# BLUE WIDGET #
Label(win, text="Red", font=myFont).grid(row=0, column=0)
ledBlueSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=updateBlue)
ledBlueSlider.grid(row=0, column=1)

# RED WIDGET #
Label(win, text="Blue", font=myFont).grid(row=1, column=0)
ledRedSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=updateRed)
ledRedSlider.grid(row=1, column=1)

# GREEN WIDGET #
Label(win, text="Green", font=myFont).grid(row=2, column=0)
ledGreenSlider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=updateGreen)
ledGreenSlider.grid(row=2, column=1)

## EXIT BUTTON ##
exitButton = Button(win, text='EXIT', font=myFont, command=exitToggle, bg='bisque2', height=1, width=24)
exitButton.grid(row=3, column=1)

win.mainloop()
