#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

Left_Motor = Motor(Port.B)
Right_Motor = Motor(Port.C)
AUTO_CAR = DriveBase(Left_Motor, Right_Motor, 56, 104)

TS = TouchSensor(Port.S1)
US = UltrasonicSensor(Port.S4)
CS = ColorSensor(Port.S3)
GS = GyroSensor(Port.S2)
SW = StopWatch()

yellow_count = 0
while(True):
    cs_val = CS.color()
    if(cs_val == Color.BLACK):
        AUTO_CAR.drive(60, 40)
    elif(cs_val == Color.WHITE):
        AUTO_CAR.drive(60, -40)

    if(SW.time() > 23000):
        break


#1번쨰 빨간색
while(True):
    gs_val = GS.angle()
    cs_val = CS.color()
    # ev3.screen.print(cs_val)

# AUTO_CAR.drive(50,gs_val)
    if(cs_val == Color.BLACK):
        AUTO_CAR.drive(60, 40)
    elif(cs_val == Color.WHITE):
        AUTO_CAR.drive(60, -40)
    elif(cs_val == Color.YELLOW):
        if(yellow_count < 1):
            AUTO_CAR.stop()
            wait(1000)
            ev3.light.on(Color.RED)
            wait(1000)
            ev3.light.on(Color.YELLOW)
            wait(1000)
            ev3.light.on(Color.GREEN)
            wait(1000)
            yellow_count += 1
        AUTO_CAR.drive(40,gs_val * 0.5)
    elif(cs_val == Color.RED):
        AUTO_CAR.stop()
        wait(500)
        ev3.speaker.play_notes(['G4/8','G4/8','A4/8','A4/8','G4/8','G4/8','E4/4'], tempo=180)
        wait(1000)
        AUTO_CAR.turn(-160)
        AUTO_CAR.straight(50)
        
        break


#2번쨰 빨간색
while(True):
    cs_val = CS.color()

# AUTO_CAR.drive(50,gs_val)
    if(cs_val == Color.BLACK):
        AUTO_CAR.drive(60, 40)
    elif(cs_val == Color.WHITE):
        AUTO_CAR.drive(60, -40)
    elif(cs_val == Color.RED):
        AUTO_CAR.stop()
        wait(500)
        ev3.speaker.say('hello')
        AUTO_CAR.turn(-160)
        AUTO_CAR.straight(50)
        break


#3번째 빨간색
while(True):
    cs_val = CS.color()
    us_val = US.distance()
    if(cs_val == Color.BLACK):
        AUTO_CAR.drive(60, 40)
        if(us_val < 180):
            AUTO_CAR.turn(90)
            AUTO_CAR.drive(40,-10)
    elif(cs_val == Color.WHITE):
        AUTO_CAR.drive(60, -40)
        if(us_val < 150):
            AUTO_CAR.turn(90)
            AUTO_CAR.drive(60,-18)
    else:
        AUTO_CAR.drive(60,-18)


#초록지점
while(True):
    cs_val = CS.color()

    if(cs_val == Color.BLACK):
        AUTO_CAR.drive(60, 40)
    elif(cs_val == Color.WHITE):
        AUTO_CAR.drive(60, -40)
    elif(cs_val == Color.GREEN):
        AUTO_CAR.stop()
        break

ev3.screen.print(SW.time())
while(True):
    pass