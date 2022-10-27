#Importing Required Libraries
import speech_recognition as sr
import pyttsx3

#Greeting and Initialization with pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)
engine.say('Go for Reggie')
engine.say('Please state a command')
engine.runAndWait()

#Building the Recognizer
#Run off of the desktop by opening terminal and typing 'python filename.py' then speak
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
            text =  r.recognize_google(audio)
            text = text.lower()
            engine.say(text)
            print('Recognized {text}')
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))
    except sr.UnknownValueError():
        engine.say('I didn\'t get that')
        r = sr.Recognizer()
        continue
