import pyautogui
import os
import pyperclip
from time import sleep

link = 'https://www.canva.com/design/DAFLpoIxGWk/6sKjJS79VjM8yuOkQncIHg/edit'

def open():
    os.system('start')
    sleep(1)
    pyautogui.write('Canva.lnk')
    pyautogui.hotkey('enter')
    sleep(3)

def newTab():
    pyautogui.click(x=107, y=52)
    sleep(1)
    pyautogui.click(146,665)
    pyautogui.write(link)
    sleep(1)
    pyautogui.press('enter')
    sleep(3)

def setTitle(title):
    pyperclip.copy(title)
    pyautogui.click(x=1218, y=685)
    sleep(1)
    pyautogui.click(x=1218, y=685)
    sleep(1)
    pyautogui.hotkey('ctrl','a')
    sleep(1)
    pyautogui.hotkey('ctrl','v')
    sleep(1)

def uploadImg():
    pyautogui.click(x=44, y=364)
    sleep(1) 
    pyautogui.click(x=313, y=245)
    sleep(1)
    pyautogui.click(x=553, y=89)
    sleep(1)
    pyautogui.write('C:\\Users\\lucif\\Desktop\\instagram\\bootpost\\')
    sleep(1) 
    pyautogui.press('enter')
    sleep(1) 
    pyautogui.click(x=317, y=547)
    sleep(1)
    pyautogui.write('post.png')
    sleep(1)
    pyautogui.press('enter')

def setImage():
    pyautogui.click(x=46, y=363)
    sleep(1)
    pyautogui.click(x=1213, y=503)
    sleep(1)
    pyautogui.click(x=1215, y=264)
    sleep(1)
    pyautogui.click(x=1215, y=326)
    sleep(1)
    pyautogui.click(x=153, y=479)
    sleep(1)
    pyautogui.moveTo(x=1214, y=589)
    sleep(1)
    pyautogui.dragTo(x=1214, y=500,button='left',duration=0.2)
    sleep(1)

def saveImage():
    pyautogui.click(x=1822, y=106)
    sleep(1)
    pyautogui.click(x=1549, y=707)
    sleep(2)
    pyautogui.click(x=1649, y=619)
    sleep(5)
    pyautogui.click(x=543, y=84)
    sleep(1)
    pyautogui.write('C:\\Users\\lucif\\Desktop\\instagram\\bootpost')
    sleep(1) 
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(x=447, y=495)
    sleep(1)
    pyautogui.write('postIg')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(x=1027, y=534)
    sleep(1)

def exit():
    pyautogui.click(x=290, y=56)
    sleep(1)
    pyautogui.hotkey('alt','tab')
    sleep(1)
    pyautogui.hotkey('ctrl','c')
    sleep(1)
    pyautogui.hotkey('alt','f4')
    sleep(1)