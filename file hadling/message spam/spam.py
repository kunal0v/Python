import pyautogui as p
import time
limit=input("Enter the limit:")

i=0
# message=input("Enter Your message:")
time.sleep(5)
while i<int(limit):
#while True:
    # p.typewrite(message)
    # p.press("Enter")
    p.hotkey("ctrl","shift","`")
    # time.sleep(1)
    # p.press("Enter")
    i+=1
    #time.sleep(10)
    
