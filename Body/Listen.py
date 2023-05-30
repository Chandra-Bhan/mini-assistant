import speech_recognition as sr
from googletrans import Translator


# 1- Listen : Hindi or English

def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening____")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
        a1=str(audio)

        #Listening Mode

        try:
            print("Recognizing____")
            query=r.recognize_google(audio,language="hi-en")

        except:
            return ""
        query =str(query).lower()
        print(query)
        return query


def TranslateHinToEng(Text):

    try:
        line=str(Text)
        translate=Translator()
        result=translate.translate(line)
        data=result.text
        print(f"You: {data}")
        return data
    except:
        return ""

def MicExecution():
    query =Listen()
    data  =TranslateHinToEng(query)
    if len(data)<=1:
        return ""

    return data

#MicExecution()