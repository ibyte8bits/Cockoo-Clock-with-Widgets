# Paul McWhorter's Visual Python Course Progams on YouTube
# Sutdent/programmer: Kens@cad2cam.com
# Date: 11/17/2021
# License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
from numpy.core.function_base import linspace
from numpy.lib.twodim_base import _trilu_indices_form_dispatcher
from vpython import *
import numpy as np
import time
from playsound import playsound
from threading import Thread

# Scene
scene = canvas(width = 400,
    height = 600,
    center = vector(0,.75,0),
    background = vector(0/255,131/255,143/255))

# Bird Movement
jump = .3
cockoo = 0
tickRadius = .005
cockoos = 0
noMoreCockoos = False

def cockoo(cockoos):
    door.color=vector(0,0,0)
    if cockoos > 12:
        cockoos = cockoos - 12
    if cockoos == 0:
        cockoos = 12
    while cockoos != 0:
        body.pos = vector(bodyX,bodyY,bodyZ + jump)
        head.pos = vector(headX,headY,headZ + jump)
        beak.pos = vector(beakX,beakY,beakZ + jump)
        playsound('cockoo.mp3')
        time.sleep(.5)
        body.pos = vector(bodyX,bodyY,bodyZ - jump)
        head.pos = vector(headX,headY,headX - jump)
        beak.pos = vector(beakX,beakY,beakZ - jump)
        cockoos = cockoos - 1
    door.color=vector(27/255,94/255,32/255)

# Face
FaceRadius = 1.1
FaceLength = .1
Face = cylinder(axis=vector(0,0,-.1),
    radius=FaceRadius,
    color=color.orange,
    pos=vector(0,0,0))

# Minute Ticks
cylRadius = .05
cylStart = .9
cylEndLength = .1
cylIncrementAngle = np.pi/60
for minute in range(0,60,1):
    MinuteAngle = minute*cylIncrementAngle
    Xpos = np.cos(MinuteAngle)
    Ypos = np.sin(MinuteAngle)
    Zpos = 0
    if minute % 5 == 0:
        CylRadius = tickRadius*3
    else:
        CylRadius = tickRadius
    Ticks = cylinder(pos=vector(Xpos,Ypos,Zpos),color=color.black,length=.1,radius=CylRadius,axis=vector(Xpos,Ypos,0))
    Ticks.rotate(MinuteAngle,axis=vector(0,0,1),origin=vector(0,0,0))
    Ticks.length=.1

# Hands
# Second
SecHandLength = .8*FaceRadius
SecHandRadius = 3*tickRadius
SecHandPos = vector(0,0,3*FaceLength)
SecondHand = cylinder(pos=SecHandPos,
    color = color.red,
    length = SecHandLength,
    radius = SecHandRadius,
    axis = vector(0,1,0))
# Minute
MinHandLength = .7*FaceRadius
MinHandRadius = 3*tickRadius
MinHandPos = vector(0,0,2*FaceLength)
MinuteHand = cylinder(pos=MinHandPos,
    color = color.white,
    length = MinHandLength,
    radius = MinHandRadius,
    axis=vector(0,1,0))
# Hour
HourHandLength = FaceRadius/2
HourHandRadius = 3*tickRadius
HourHandPosition = vector(0,0,FaceLength)
HourHand = cylinder(pos=HourHandPosition,
    color = color.blue,
    length = HourHandLength,
    radius = HourHandRadius,
    axis = vector(0,1,0))

# Hubs
# Hour
HourHubRadius = 4 * HourHandRadius
HourHubLength = FaceLength * 7 / 4
HourHubPosition = vector(0,0,0)
HourHub = cylinder(axis=vector(0,0,1),
    length = HourHubLength,
    radius =HourHubRadius,
    color=color.blue,
    pos=HourHubPosition)

# Minute
MinHubRadius = 3*MinHandRadius
MinHubLength = FaceLength * 5 / 2
MinHubPosition = vector(0,0,FaceLength)
SecHub = cylinder(axis=vector(0,0,FaceLength + .2),
    radius=MinHubRadius,
    length=MinHubLength,
    color=color.white,
    pos=vector(0,0,0))

# Second
SecHubRadius = 2*SecHandRadius
SecHubLength = FaceLength * 11 / 4
SecHubPosition = vector(0,0,FaceLength)
HourHub = cylinder(axis=vector(0,0,1),
    radius=SecHubRadius,
    length=SecHubLength,
    color=color.red,
    pos=SecHubPosition)

# Time
localTime = time.localtime()
InitialSeconds = float(localTime.tm_sec)
InitialMinutes = float(localTime.tm_min)
Hour12 = (localTime.tm_hour)%12
InitialHours   = float(Hour12)
SecondAngle = -( InitialSeconds / 60 ) * 2 * np.pi  
MinuteAngle = -( InitialMinutes / 60 + ( ( InitialSeconds / 60 ) / 60 )  ) * 2 * np.pi
HourAngle   = -( ( InitialHours / 12 + ( InitialMinutes / 60 ) / 12 ) + ( ( ( InitialSeconds / 60 ) / 60 ) / 12 ) ) * 2 * np.pi
SecondHand.rotate(SecondAngle,
    axis = vector(0,0,1),
    origin = vector(0,0,3*FaceLength))
MinuteHand.rotate(MinuteAngle,
    axis=vector(0,0,1),
    origin = vector(0,0,2*FaceLength))
HourHand.rotate(HourAngle,
    axis=vector(0,0,1),
    origin = vector(0,0,FaceLength))

SecondAngle = -np.pi/30
OldTime = localTime.tm_sec
NewTime = OldTime

# Case
# Body
boxColor = vector(80/255,40/255,35/255)
boxWidth = 3.0
boxHeight = 3.0
boxDepth = 1.5
boxOrigin = vector(0,0,-(.76))
bodyBox = box(size=vector(boxWidth, boxHeight, boxDepth), 
    color=boxColor, 
    pos=boxOrigin,)

# Peak
peakColor = boxColor
peakWidth = 3.0 * .7071
peakHeight = peakWidth
peakDepth = boxDepth
peak = box(size=vector(peakWidth,peakHeight,peakDepth),
    color=peakColor,
    pos=vector(0,1.5,-.76))
peak.rotate(angle=np.pi/4,axis=vector(0,0,1),origin=vector(0,1.5,0))

# Door
doorColor = vector(27/255,94/255,32/255)
doorHeight = .4
doorWidth = .4
doorDepth = .1
doorOrigin = vector(0, 1.75, -(int(doorDepth/2)))
door = box(color=doorColor,
    size=vector(doorWidth,doorHeight,doorDepth),
    pos=doorOrigin)

# Bird
# Body
bodyColor = vector(1,1,0)
bodyRadius = .1
bodyX = 0
bodyY = 1.75
bodyZ = -.3
body = sphere(radius=bodyRadius,
    color=bodyColor,
    pos=vector(bodyX,bodyY,bodyZ))
# Head
headColor = vector(1,1,0)
headRadius = .06
headX = 0
headY = bodyY + .075
headZ = bodyZ + .12
head = sphere(radius=headRadius,
    color=headColor,
    pos=vector(headX,headY,headZ))
# Beak
beakColor = vector(1,0,0)
beakRadius = .04
beakAxis = vector(0,0,.15)
beakX = headX
beakY = headY
beakZ = headZ
beakPos = vector(beakX, beakY, beakZ)
beak = cone(pos=beakPos,
    axis=beakAxis,
    color=beakColor,
    radius=beakRadius)

# Numbers
textRadius = FaceRadius * .7
textColor = vector(92/255,107/255,192/255)
textHeight = FaceRadius/6
for number in range(1,13,1):
    textAngle = np.pi/6
    textPosition = vector(textRadius*np.sin(textAngle*number),
        textRadius*np.cos(textAngle*number)-textHeight/2,
        0)
    text(text=str(number),
        pos=textPosition,
        color=textColor,
        height=textHeight,
        align='center')

def showBird(x):
    if x.checked == True:
        door.color=vector(0,0,0)
        body.pos = vector(bodyX,bodyY,bodyZ + jump)
        head.pos = vector(headX,headY,headZ + jump)
        beak.pos = vector(beakX,beakY,beakZ + jump)
    if x.checked == False:
        body.pos = vector(bodyX,bodyY,bodyZ - jump)
        head.pos = vector(headX,headY,headX - jump)
        beak.pos = vector(beakX,beakY,beakZ - jump)
        door.color=vector(27/255,94/255,32/255)  

checkbox(bind=showBird, text='Show the birdie ')
wtext(text='\n')

def hearBird(x):
    if x.checked == True:
        playsound('cockoo.mp3')
        x.checked = False
    
checkbox(bind=hearBird, text='Hear the birdie ')
wtext(text='\n')

def birdJump(x):
    global jump
    jump = x.value

wtext(text='\nHow far do you want the bird come out.\n')
wtext(text='Normal                                                                   Farthest\n')
slider(bind=birdJump, vertical=False, min=.3, max=.5, value=.3)
wtext(text='\nClick "Show the birdie" after setting slider.')


while True:
    rate(10)
    if OldTime != NewTime:
        SecondHand.rotate(SecondAngle,
            axis = vector(0,0,1),
            origin = vector(0,0,3*FaceLength))
        MinuteHand.rotate(SecondAngle/60,
            axis=vector(0,0,1),
            origin = vector(0,0,2*FaceLength))
        HourHand.rotate(SecondAngle/720,
            axis=vector(0,0,1),
            origin = vector(0,0,FaceLength))
        CurrentTime = time.localtime()
        OldTime = CurrentTime.tm_sec
        print(CurrentTime.tm_hour, ":", CurrentTime.tm_min, ":", CurrentTime.tm_sec)
        if CurrentTime.tm_min == 0 and CurrentTime.tm_sec == 0 and noMoreCockoos != True:
            noMoreCockoos = True
            CockooThread = Thread(target=cockoo, args=(CurrentTime.tm_hour,))
            CockooThread.daemon = True
            CockooThread.start()
        if ( CurrentTime.tm_min == 15 or CurrentTime.tm_min == 30 or CurrentTime.tm_min == 45 ) and CurrentTime.tm_sec == 0 and noMoreCockoos != True:
            noMoreCockoos = True
            CockooThread = Thread(target=cockoo,args=(1,))
            CockooThread.daemon = True
            CockooThread.start()
        if CurrentTime.tm_min == 7 or CurrentTime.tm_min == 22 or CurrentTime.tm_min == 37 or CurrentTime.tm_min == 51:
            noMoreCockoos = False

    CurrentTime = time.localtime()
    NewTime = CurrentTime.tm_sec
