import pyttsx3     #this whole code is to check the voices that are available
engine = pyttsx3.init()
voices = engine.getProperty('voices')      
for i in voices:
    print(i)
