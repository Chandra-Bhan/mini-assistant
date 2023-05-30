import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body.Speak import Speak

def OpenExe(Query):
    Query=str(Query).lower()
    Speak("OK! Sir")
    if "visit" in Query:
        Nameofweb=Query.replace("visit ","").replace(" ","")
        Link=f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    elif "launch" in Query:
        Nameofweb=Query.replace("launch ","").replace(" ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    elif "open" in Query:
        Nameoftheapp=Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in Query:
        Nameoftheapp=Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    else:
        return False

# OpenExe("start powerpoint")