#need to install two modules
#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr
#import pyaudio

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Enter Anything:")
    audio=r.listen(source)

    try:
        
        text=r.recognize_google(audio)
        print("You said: {}" .format(text))
    except:
        print("Sorry cound not recognize your voice")
        
