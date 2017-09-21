import voice as voice
import wikipedia
import webbrowser

def search(search_text):
	value = wikipedia_search(search_text)
	print(value)
	if value == 0:
		search_fail()
	if value == 1:
		print("value == 1")
		voice.system_say("You are welcome. Feel free to ask me for anything else.")

def wikipedia_search(search_text):
	search_results = wikipedia.search(search_text)
	print(search_results)
	if len(search_results) == 0:
		return 0
	index = 0
	page = wikipedia.page(search_results[index])
	open_website(page.url)
	exit_keywords = ['leave', 'nevermind', 'exit']
	no_keywords = ['no', 'nope', 'not really', 'not']
	yes_keywords = ['yes', 'yep', 'sure']
	correct = voice.audio_recognition()
	while(correct.lower() not in exit_keywords):
		#correct = voice.audio_recognition()
		voice.system_say(correct)
		if correct.lower() in no_keywords:
			if len(search_results) < index + 2:
				search_fail()
				return 0
			index+=1
			page = wikipedia.page(search_results[index])
			open_website(page.url)
			correct = voice.audio_recognition()
		if correct.lower() in yes_keywords:
			print("yes_keywords")
			return 1

def wikipedia_confirm():
	voice.system_say("Is this what you are looking for?")

def search_fail():
	voice.system_say("Sorry Sir, I did not find what you were looking for.")

def open_website(url):
	webbrowser.open_new(url)
	wikipedia_confirm()