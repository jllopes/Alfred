import voice as voice
import search as search
import random

def say_quote():
	quotes = ['I never wanted you to come back to Gotham. I always knew there was nothing for you here, except pain and tragedy. And I wanted something more for you than that. I still do.', 'We burned the forest down.', 'Endure, Mister Wayne. Take it. They will hate you for it, but that is the point of the Batman. He can be the outcast, he can make the choice that no one else can make, the right choice.', 'Some men just want to watch the world burn.', 'I have sewn you up, I have set your bones, but I will not bury you. I have buried enough members of the Wayne family.', 'He is not being a hero. He is being something more.', 'I am so sorry. I failed you. You trusted me and I failed you', 'Rachel believed in what you stood for, what we stand for. Gotham needs you.']
	quote_nr = random.randrange(7)
	voice.system_say(quotes[quote_nr])

def get_requests():
	voice.system_say("How can I help you, Sir?")
	exit_keywords = ['goodbye', 'bye', 'later', 'exit', 'close']
	quotes_keywords = ['quotes', 'phrases']
	search_keyword = 'search '
	request = voice.audio_recognition()
	while(request.lower() not in exit_keywords):
		if request.lower() in quotes_keywords:
			say_quote()
		if search_keyword in request.lower():
			full_text = request.split(search_keyword)
			search_text = full_text[1]
			search.wikipedia_search(search_text)
		request = voice.audio_recognition()
		print(request)

if __name__ == '__main__':
	get_requests()