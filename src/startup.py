import datetime
from src.Features.speak import speak #local module
import os



def wishme(): #wish function + clear console 
    hour= int(datetime.datetime.now().hour)
    if hour<=12:
        speak("Good Morning!")
    elif hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    os.system('cls')
