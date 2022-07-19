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
ev3 = EV3Brick()    #컨드롤러


# Write your program here.
ev3.speaker.beep()  #스피커

# ev3.light.on(Color.RED)
# wait(1000)
# ev3.light.off()
# wait(100)

# ev3.light.on(Color.RED)
# wait(1000)
# ev3.light.off()
# wait(100)

# ev3.light.on(Color.RED)
# wait(1000)
# ev3.light.off()
# wait(100)

# led가 3회 점멸하도록 하시오

# ev3.speaker.beep(frequency = 500, duration = 100)
# ev3.speaker.play_notes(['C4/4','D4/4','E4/4'], tempo=180)
# ev3.speaker.say('ev3 python hello hi')

# ev3.speaker.set_volume(10)
# ev3.speaker.play_notes(['C4/4','D4/4','E4/4'], tempo=180)

# ev3.speaker.set_volume(30)
# ev3.speaker.play_notes(['C4/4','D4/4','E4/4'], tempo=180)

# ev3.speaker.set_volume(70)
# ev3.speaker.play_notes(['C4/4','D4/4','E4/4'], tempo=180)

ev3.screen.clear()
wait(1000)
# wait(1000)
# ev3.screen.print('Hye Min A \n Sa Rang Hae')
# wait(5000)
# ev3.screen.print('1')
# ev3.screen.print('2')
# ev3.screen.print('3')
# ev3.screen.print('4')
# ev3.screen.print('5')
# ev3.screen.print('6')
# ev3.screen.print('7')

# ev3.screen.draw_text(100,100, 'ev3')
# ev3.screen.draw_pixel(10,50)
# ev3.screen.draw_line(10,10,50,50)
# ev3.screen.draw_box(10,10,50,50,r=10,fill=True)   #r=10은 모서리를 둥글게 만들어주는 정도, (fill) 색채우기(검은색)
# ev3.screen.draw_circle(50,50,20)
# ev3.screen.print(ev3.screen.width)
# ev3.screen.print(ev3.screen.height)

# while(True):
#     b_val = ev3.buttons.pressed()       #버튼 입력
#     ev3.screen.print(b_val)
#     if(b_val == [Button.UP]):       #입력받은 버튼이 업버튼이면
#         ev3.light.on(Color.RED)         #빨간색 빛 출력
#         # wait(1000)
#     elif(b_val == [Button.DOWN]):       #입력받은 버튼이 다운버튼이면
#         ev3.light.on(Color.YELLOW)      #노란색 빛 출력
#     elif(b_val == [Button.LEFT, Button.RIGHT]):
#         ev3.light.on(Color.ORANGE)
#     else:
#         ev3.light.off()

LM = Motor(Port.B)
RM = Motor(Port.C)
car = DriveBase(LM, RM, 56, 104)     #지름 = 56(지름) * 28(폭) 타이어에 제원값이 적혀있음 

TS = TouchSensor(Port.S1)
US = UltrasonicSensor(Port.S4)
CS = ColorSensor(Port.S3)
GS = GyroSensor(Port.S2)

# while(True):                          터치센서 기본예제
#     touch_sensor = TS.pressed()
#     # ev3.screen.print(touch_sensor)
#     if(touch_sensor):
#         ev3.screen.print('OOOOO')
#     else:
#         ev3.screen.print('XXXXX')


while(True):
    # a = TS.pressed()
    # if(a):
    #     car.stop()
        
    # else:
    #     car.drive(100,0)
    # us_val = US.distance()      #MAX=2550, min=30 (mm)
    # ev3.screen.print(us_val)

    # if(us_val > 300):                       #초음파센서 활용
    #     car.drive(100,0)
    # elif(us_val > 300 and us_val <400):
    #     car.stop()
    # else:
    #     car.drive(-100,0)
    # cs_val = CS.color()
    # cs_val = CS.ambient()             #빛 흡수량
    # cs_val = CS.reflection()            #지표면에 의해 반사되는 빛 흡수량
    #CS.rgb() = [100, 100, 100]
    # if(cs_val <5):
    #     car.stop()
    # else:
    #     car.drive(100,0)
    # ev3.screen.print(cs_val)
    
    gs_val = GS.angle()
    # ev3.screen.print(gs_val)
    # if(gs_val == 0):
    #     car.drive(50,0)
    # elif(gs_val < 0 and gs_val > -90):
    #     car.drive(50, -10)
    # elif(gs_val > 0 and gs_val < 90):
    #     car.drive(50, 10)
    # elif:
    #     car.drive(50,50)              #구닥다리
    car.drive(50, gs_val)
# car.settings(100, 10, 1000, 10) # , , 회전가속도, 회전 각속도

# car.straight(100) #mm단위  직진
# car.turn(-180)

# while(True):
#     car.drive(100, 100) #직진속도, 회전속도

# m.run(100)
# wait(1000)

# LM.run_time(100, 3000)
# # LM.run_angle(100, 360)

# RM.run_time(100, 3000)
# # RM.run_angle(100,360)

# LM.run(200)
# RM.run(200)
# wait(5000)

# LM.stop
# RM.stop
# wait(3000)
# LM.run_angle(100,360)
# LM.run(200)
# RM.run(200)
# wait(5000)

# LM.run(100)
# RM.run(100)
# wait(1000)

# LM.stop()
# RM.stop()

# LM.run(-100)
# RM.run(100)
# wait(1000)

# RM.stop()   #관성에 의해 천천히 정지
# RM.brake()  #팍 정지
# RM.hold()   #안움직임

# while(True):
#     s = RM.speed()
#     a = RM.angle        #프로그램을 실행시켰을 떄가 기준(0도)임 바퀴가 어느 각도로 시작했건 그 각도가 0도로 시작
#     # ev3.screen.print(a)
    
#     # d = LM.run(s)
#     LM.run_target(100,a)