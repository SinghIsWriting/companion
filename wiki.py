from wikipedia import set_lang, summary
from datetime import datetime
from path import path
from speak import speak

def wik(topic):
	try:
		set_lang("en")
		result = summary(topic, sentences = 2)

		with open("txt/wikiLogs.txt","a", encoding="utf-8") as f:
			f.write(f"{topic.title()}:\n{result}\n[{datetime.now()}]\n\n")
		
		print(result)
		speak(result, "wiki.mp3")
	except:
		er = "Sorry, I didn't find anything "
		print(er)
def wk(top):
	if top == "about" or top == "tell me about":
		pass
	else:
		wik(top)

if __name__ == "__main__":
	l = input("Enter: ")
	wik(l)
