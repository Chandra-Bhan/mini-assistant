import speech_recognition as sr
from googletrans import Translator
import os


# 1- Listen : Hindi or English

def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening---")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
        #Listening Mode

        try:
            print("Recognizing---")
            query=r.recognize_google(audio,language="en")
        except:
            return ""
        query =str(query).lower()
        return query

def TranslateHinToEng(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"You: {data}")
    return data


def WakeupDetected():
    data=Listen().lower()
    query=TranslateHinToEng(data).lower()
    if "wake up" in data:
        os.startfile(r'D:\Learning\GUI Jarvis\Main.py')
    else:
        pass

while True:
    WakeupDetected()