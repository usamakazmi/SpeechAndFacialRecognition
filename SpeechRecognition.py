# pip install SpeechRecognition
# pip install PyAudio

from email.mime import audio
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('{}'.format(text))
    except:
        print('Sorry I did not understand, please repeat...')
