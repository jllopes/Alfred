import voice as voice
import wikipedia
import webbrowser

def search(search_text):
	if wikipedia_search(search_text) == 0:
		search_fail()

def wikipedia_search(search_text):
	search_results = wikipedia.search(search_text)
	if len(search_results) == 0:
		return 0
	index = 0
	page = wikipedia.page(search_results[index])
	correct = open_website(page.url)
	exit_keywords = ['leave', 'nevermind', 'exit']
	no_keywords = ['no', 'nope', 'not really', 'not']
	yes_keywords = ['yes', 'yeap', 'sure']
	while(correct.lower() not in exit_keywords):
		print(correct)
		if correct.lower() in no_keywords:
			if len(search_results) < index:
				wikipedia_fail()
				return 0
			index+=1
			page = wikipedia.page(search_results[index])
			correct = open_website(page.url)
		if correct.lower() in yes_keywords:
			return 1
		correct = audio_recognition()

def wikipedia_confirm():
	voice.system_say("Is this what you are looking for?")

def search_fail():
	voice.system_say("Sorry Sir, I did not find what you were looking for.")

def open_website(url):
	webbrowser.open_new(url)
	wikipedia_confirm()
	correct = voice.audio_recognition()
	return correct