#Library Importation
import speech_recognition as sr
import pyttsx3 

#Setting Voice Assistant Name
name = 'Reggie'

#Speaking Text
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)
engine.say('Go for Reggie')
engine.say('Please state a command')
engine.runAndWait()

#Listening for Events
def onStart(name):
    print('Starting', name)

def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('Test successful.')
engine.runAndWait()

#using SR For Recieving Input
#Obtaining Audio from Microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Awaiting command...')
    audio = r.listen(source)

#Recognize Speech Using Google Speech Recognition
try:
    print('Reggie thinks you said ' + r.recognize_google(audio))
except sr.UnknownValueError:
    print('Reggie didn\'t understand what you said')
except sr.RequestError as e:
    print('Could not request results from Google Speech Recognition service; {0}'.format(e))