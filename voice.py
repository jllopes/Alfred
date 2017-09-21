import speech_recognition as speech
from os import system

rec = speech.Recognizer()

def system_say(text):
	system("say " + text)

def audio_detection():
	with speech.Microphone() as source:
		audio = rec.listen(source)
	return audio

def audio_recognition():
	text = None
	while (text is None):
		try:
			text = rec.recognize_google(audio_detection())
		except speech.UnknownValueError:
			text = None
	return text

