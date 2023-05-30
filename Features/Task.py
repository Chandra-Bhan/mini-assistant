import datetime
import wikipedia
import pywhatkit
from Body.Speak import Speak

def Date():
    date=datetime.date.today()
    Speak(date)
def Day():
    day=datetime.datetime.now().strftime("%A")
    Speak(day)
def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Speak(time)

def NonInputExecution(query):
    query=str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    else:
        pass

def InputExecution(tag,query):
    if "wikipedia" in tag:
        try:
            name=str(query).replace("who is","").replace("about","").replace("what is","")
            result=wikipedia.summary(name)

            print(result)
        except:
            Speak("Sorry! Sir Something is wrong")
        # count=0
        # res=""
        # for r in result:
        #     count+=1
        #     res=res+r
        #     if(count==500):
        #         break
        # print(res)
        # Speak(res)
    elif "google" in tag:
        query=str(query).replace("google","").replace("search on google","")
        pywhatkit.search((query))
    else:
        pass

#InputExecution("google","ho is salman khan")
#NonInputExecution("time")