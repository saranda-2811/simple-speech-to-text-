!pip install SpeechRecognition
import speech_recognition as sr
r=sr.Recognizer()
h=sr.AudioFile(r'C:\Users\saran\Downloads\audio_test1.wav')
with h as source:
    audio = r.record(source)
type(audio)
r.recognize_google(audio)
