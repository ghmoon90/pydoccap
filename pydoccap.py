#import pyautogui
#import pydirectinput as pydi
#import win32api, win32con 
#import keyboard as kbd
from pynput.keyboard import Key, Controller
keyboard = Controller()

import time as tm
from PIL import ImageGrab 
from functools import partial
from tkinter import *
import os 

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
imf = ImageGrab.grab(bbox=None)
imf.size


def testcap(bbox_):
    imf = ImageGrab.grab(bbox=bbox_)
    imf.save('./test.png')
    imf.show()



window=Tk()
window.title("pydoccap.py")

str_right = StringVar(window,'right')
str_bottom = StringVar(window,'bottom')
str_left = StringVar(window,'left')
str_top  = StringVar(window,'top')
str_title = StringVar(window,'doc title')
str_pages = StringVar(window,'pages')


area_right  = 0
area_bottom = 0
area_left   = 0
area_top    = 0
area        = [0 , 0 , 0 , 0]
sz_doctitle = 'any_doc'
pages       = 0

# previous setting load
def loadtext():
    global str_right, str_bottom, str_left, str_top, str_title, str_pages, area_right, area_bottom, area_left, area_top, area, sz_doctitle, pages
    with open("./pydoccap.dat",'r') as fhd:
        lines = fhd.readlines()
        
    newline = []
    for line in lines:
        newline.append(line.replace('\n',''))
    lines = newline
    print(lines)

    str_left.set(lines[0])
    str_top.set(lines[1])
    str_right.set(lines[2])
    str_bottom.set(lines[3])
    str_title.set(lines[4])
    str_pages.set(lines[5])
    area_left   =int(lines[0])
    area_top    =int(lines[1])
    area_right  =int(lines[2])
    area_bottom =int(lines[3])
    sz_doctitle = lines[4]
    pages       = int(lines[5])
    area        = [area_left , area_top , area_right , area_bottom]

# save the info when user push the set button
def savetext():
    global  area_right, area_bottom, area_left, area_top, sz_doctitle, pages
    with open("./pydoccap.dat",'w') as fhd:
        fhd.write(str(area_left) + "\n")
        fhd.write(str(area_top) + "\n")
        fhd.write(str(area_right) + "\n")
        fhd.write(str(area_bottom) + "\n")
        fhd.write(sz_doctitle + "\n")
        fhd.write(str(pages) )


loadtext()
tbox_right = Entry(window, width=20, textvariable=str_right)
tbox_bottom = Entry(window, width=20, textvariable=str_bottom)

tbox_left = Entry(window, width=20, textvariable=str_left)
tbox_top  = Entry(window, width=20, textvariable=str_top)

tbox_title = Entry(window, width=20, textvariable=str_title)

#tbox_title = Text(window, width=20, height=3)
tbox_pages = Entry(window, width=20, textvariable=str_pages)


stext_right  = Label(window,text='Area.right:', width=10,height=1)
stext_bottom= Label(window,text='Area.bottom:', width=10,height=1)
stext_left  = Label(window,text='Area.left:', width=10,height=1)
stext_top = Label(window,text='Area.top:', width=10,height=1)
stext_doctitle = Label(window,text='document name:', width=20,height=1)
stext_pages = Label(window,text='#pages:', width=20,height=1)

# check the area 
def test_act():
    global area
    right = int(str_right.get())
    bottom = int(str_bottom.get())
    left = int(str_left.get())
    top = int(str_top.get())
    area = [left, top, right, bottom]
    print(area)
    testcap([left, top, right, bottom])

# set the area and document tilte, number of pages
def set_act():
    global area_right, area_bottom, area_left, area_top, area, sz_doctitle, pages
    area_right  = int(str_right.get())
    area_bottom = int(str_bottom.get())
    area_left   = int(str_left.get())
    area_top    = int(str_top.get())
    area        = [area_left, area_top, area_right, area_bottom]
    print(area)
    sz_doctitle    = str_title.get()
    print('document title: '+sz_doctitle)
    pages       = int(str_pages.get())
    print('number of pages : '+ str(pages))
    savetext()
    os.mkdir('./'+sz_doctitle,0x777)
    print('directory made')



def run_act():
    global area, sz_doctitle, pages
    print('run act')

    # activate the loop after 3 seconds
    for k in range(0,3):
        print(k)
        tm.sleep(1)

    # sampling and move to next page
    # if keyinput not works, use administrator right or super user 
    for k_page in range(0,pages):
        print(k_page+1)
        sz_title = './'+sz_doctitle+'/'+sz_doctitle+'_'+str(k_page+1)+'.png'
        imk = ImageGrab.grab(bbox = area) 
        imk.save(sz_title)
        print('captured :'+sz_title)
        tm.sleep(0.5)   
        #win32api.keybd_event(0x27, 0, 0, 0)
        #win32api.keybd_event(0x27, 0, win32con.KEYEVENTF_KEYUP, 0)
        if (k_page+1) < pages:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print('move to next page')
            tm.sleep(2)        

    print('run complete!')



tbox_left.grid(column = 20 , row = 10)
tbox_top.grid(column = 20 , row = 20)

tbox_right.grid(column = 20 , row = 30)
tbox_bottom.grid(column = 20 , row = 40)


stext_right.grid(column = 5 , row = 30)
stext_bottom.grid(column = 5 , row = 40)
stext_left.grid(column = 5 , row = 10)
stext_top.grid(column = 5 , row = 20)
stext_doctitle.grid(column = 5 , row = 60)
stext_pages.grid(column = 5 , row = 70)


test_action=Button(window, text="image Testing" , command = test_act, width = 20 , height= 2 )
test_action.grid(column=20, row=50)


tbox_title.grid(column = 20 , row = 60)
tbox_pages.grid(column = 20 , row = 70)

set_Action = Button(window, text="set"  , command = set_act, width = 20 , height= 2 )
set_Action.grid(column=20, row=80)

run_Action = Button(window, text="run capture"  , command = run_act, width = 20 , height= 2 )
run_Action.grid(column=20, row=90)
window.mainloop()

#papertitle = input('What is title of paper?')
#pages = int(input('How many pages?'))


