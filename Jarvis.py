# starting page fo this application.

print(">> Starting The Jarvis: Wait For Some Seconds")

from Body.Speak import Speak
#from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
from Features.Clap import Tester
from Main import MainTaskExecution


# Speak(">> Starting The Jarvis: Wait For Some Seconds")

def MainExe():

    Speak("Hello Sir")
    Speak("I'm jarvis, I'm Ready To Assist You Sir.")

    while True:
        Data=MicExecution()
        Data=str(Data)

        ValueReturn=MainTaskExecution(Data)
        if ValueReturn==True:
            ValueReturn=""
            pass
        elif len(Data)<=1:
            continue
        else:
            pass

        Speak(ValueReturn)

def ClapDetect():   
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">>Clap Detected")
        print("")
        MainExe()
    else:
        pass

# ClapDetect()
MainExe()