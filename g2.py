import os
import pyttsx3
import speech_recognition as s
from time import ctime

import os
import time

p1 = pyttsx3.init()

def speak(audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = s.Recognizer()
    with s.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    

    # Speech recognition using Google Speech Recognition
    data = ""
    try:    
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except s.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except s.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
   
def says(data):
    x = ['good','fine','great']
    bad = ['bad','fuck','shit']
    pos = 0
    neg = 0

    for i in range(len(x)):
        if(x[i] in data):
            #p1.say("It is Positive Word")
            #p1.runAndWait()
            print("first if")
            pos = pos + 1
        elif(bad[i] in data):
            neg += 1
            print("second if")
        else:
            pass
    if(pos > neg):
        p1.say("It is Positive Word")
        p1.runAndWait()
    else:
        p1.say("It is Negative Word")
        p1.runAndWait()


time.sleep(2)
p1.say("Hi Gaurav What can i do for you")
p1.runAndWait()
while 1:
    data = recordAudio()
    says(data)