from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import math
mouse=Controller()
time.sleep(5)
degree=20 #DO 50 AT MOST, controls size of graph drawn
tpi=1 #time to draw full graph
addaxis=False #decides if axis are drawn or not
aximarkerthickness=5 #controls thickness of the marker on the axis (which aren't even drawn properly by the way)
"""
READ ME

this code will graph the given equation: y=x or y=2x so on

when ran it will wait then take control of your mouse to draw it on your screen so open some drawing application (this is made for microsoft paint) so it's actually drawn
please do not have anything important open as it might click on something you don't want it to

you give the equation in the form of the order of operation
here are some examples because you don't need an explanation beyond that

y=[["+","x"]]
this will graph y=x

y=[["+","x","*",2]]
graphs y=2x

y=[["+","x"],["sin",0]]
graphs y=sin(x)

y=[["+","x"],["root",2]]
graphs y=root(x)

when making an operation if x is included you can add one more instruction in that same instruction
example of what this means
y=[["+","x","*",3]] is valid

y=[["+",2,"*","x"]] is not valid

y=[["+","x"]] is valid

y=[["+",2]] is valid



I AM AWARE OF THE BUG WITH ROOTS THIS PROJECT IS ALREADY IRRELEVANT SO I WON'T FIX IT
"""
#elipsies ["+",9*49],["-","x","**",2,"*",49],["/",9],["root",2]
y=[["+",49*49],["-","x","**",2,"*",49],["/",49],["root",2]]



tpi/=(degree*10)
if addaxis:
    mouse.position=(250,500)
    mouse.press(Button.left)
    mouse.position=(1500,500)
    mouse.release(Button.left)
    mouse.position=(500,500)
    mouse.press(Button.left)
    mouse.position=(100,500)
    mouse.release(Button.left)
    mouse.position=(650,300)
    mouse.press(Button.left)
    mouse.position=(650,700)
    mouse.release(Button.left)
    extrax=0
    for i in range(21):
        extrax+=degree
        mouse.position=(1*degree+(650*1.25)-extrax,500-aximarkerthickness)
        mouse.press(Button.left)
        mouse.position=(1*degree+(650*1.25)-extrax,500+aximarkerthickness)
        mouse.release(Button.left)
    extray=0
    for i in range(21):
        extray+=degree
        mouse.position=(650+aximarkerthickness,1*degree+500-extray)
        mouse.press(Button.left)
        mouse.position=(650-aximarkerthickness,1*degree+500-extray)
        mouse.release(Button.left)
roots=0
for j in y:
    if j[0]=="root":
        roots+=1
rootpon=[]
for j in range(roots):
    rootpon.append(False)
for j in range(int(2**roots)):
    mouse.release(Button.left)
    for i in range(-10*degree,10*degree+1):
        try:
            time.sleep(tpi)
            x=i/degree
            cyv=0
            nor=0
            for u in y:
                if "x"==u[1]:
                    tempval=x
                    for b in range(2,len(u),2):
                        if u[b]=="+":
                            tempval+=u[b+1]
                        elif u[b]=="-":
                            tempval-=u[b+1]
                        elif u[b]=="/":
                            tempval/=u[b+1]
                        elif u[b]=="*":
                            tempval*=u[b+1]
                        elif u[b]=="**":
                            tempval**=u[b+1]
                        elif u[b]=="%":
                            tempval%=u[b+1]
                        elif u[b]=="sin":
                            tempval=math.sin(tempval)
                else:
                    tempval=u[1]
                if u[0]=="+":
                    cyv+=tempval
                elif u[0]=="-":
                    cyv-=tempval
                elif u[0]=="/":
                    cyv/=tempval
                elif u[0]=="*":
                    cyv*=tempval
                elif u[0]=="**":
                    cyv**=tempval
                elif u[0]=="%":
                    cyv%=tempval
                elif u[0]=="sin":
                    cyv=math.sin(cyv)
                elif u[0]=="cos":
                    cyv=math.cos(cyv)
                elif u[0]=="tan":
                    cyv=math.tan(cyv)
                elif u[0]=="sinh":
                    cyv=math.sinh(cyv)
                elif u[0]=="root":
                    if rootpon[nor]:
                        cyv=-cyv**(1/tempval)
                    else:
                        cyv=cyv**(1/tempval)
                    nor+=1
            # future me, use this to override the homemade math system
            #cyv=(16-(x)**2)**(1/2)+(9-(x)**2)**(1/2)-5
            xpos=650+(x*degree)
            ypos=500-(cyv*degree)
            if xpos>200 and xpos<1800 and ypos>300 and ypos<700:
                mouse.position=(xpos,ypos)
                mouse.press(Button.left)
            else:
                mouse.release(Button.left)
        except:
            pass
    if len(rootpon)!=0:
        if rootpon[0]:
            rootpon[0]=False
            for n in range(1,len(rootpon)-1):
                if rootpon[n]:
                    rootpon[n]=False
                else:
                    break
        else:
            rootpon[0]=True
mouse.release(Button.left)
def on_press(key):
    pass
def on_release(key):
    if key==keyboard.Key.esc:
        listener.stop()
    if key==keyboard.Key.up:
        mouse.release(Button.left)
        mouse.position=(mouse.position[0],300)
        mouse.press(Button.left)
        mouse.position=(mouse.position[0],700)
        mouse.release(Button.left)
        try:
            print("("+str((mouse.position[0]-650)/degree)+","+str(yv[200+(mouse.position[0]-650)])+")")
        except:
            print("no real value for this point")
#with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
#    listener.join()
