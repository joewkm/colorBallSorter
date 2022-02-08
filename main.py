#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
# Create your objects here

 
# Initialize the EV3 Brick.
ev3 = EV3Brick()
light = ColorSensor (Port.S1)
Redirect = Motor(Port.D)
Gate = Motor(Port.B)
Filter = Motor(Port.C)
TouchSensor = TouchSensor (Port.S2)

global total_black
global total_brown


Filter.reset_angle(0)
Filter.run_angle (2000, -360)

def dispatch():
    Filter.run_angle (2000, -360)

def redirectLeft():
    Gate.run_angle(2000,360)     
    Redirect.run_angle(-6000, -45)
    Redirect.run_angle(-6000, 45)  
    Redirect.reset_angle(0)

def redirectRight():
    Gate.run_angle(2000,360)
    Redirect.run_angle(-6000, 45)
    Redirect.run_angle(-6000, -45)
    Redirect.reset_angle(0)


def StartDispatchBall():
    print('start dispatchball')


def DetectColor():

    global total_black
    global total_brown

    dispatchBall = 0
    color_white = 0
    color_black = 0
    color_brown = 0
    for i in range(10):
        color = light.color()
        if color == color.BLACK:
            color_black += 1
        if color == color.BROWN or color == color.RED:
            color_brown += 1
        if color == color.WHITE:
            color_black = 0
            color_brown = 0
            break

    if color_brown > color_black:
        total_brown += 1
        dispatchBall = 1
        redirectLeft()

    if color_brown < color_black:
        total_black += 1
        dispatchBall = 1
        redirectRight()

    if dispatchBall == 1:
        dispatch()

# Write your program here
Gate.reset_angle(0)
Redirect.reset_angle(0)
Filter.reset_angle(0)

total_black = 0
total_brown = 0

while True:
    DetectColor()
     
    #kill code
    if Button.UP in ev3.buttons.pressed():
        print('program exit')
        break
    if TouchSensor.pressed() == True:
        print('program exit')
        break

print('Total black: ', total_black)
print('Total brown: ', total_brown)

total = total_black + total_brown
print('Total: ', total)