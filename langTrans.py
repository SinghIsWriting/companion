from colorama import Fore, init
init(autoreset=True)
from googletrans import Translator
from datetime import datetime
from speak import speak
from path import path

translator = Translator()

def tr(word):
	try:
		translation = translator.translate(word,src="en",dest="hi")
		print(f"{Fore.CYAN}Translated meaning=",translation.text)
		speak(translation.text, "langTrans.mp3")
	except:
		print(f"{Fore.RED}\nOpps, something went wrong!\n")
	finally:
		translation = translator.translate(word,src="en",dest="hi")
		ff =  open(path+"txt/langTrans.txt",'a', encoding="utf-8")
		l = ("Text: "+str(translation.origin.title())+"\n"+"Translation: "+str(translation.text)+"\n"+"Pronunciation: "+str(translation.pronunciation)+"\n"+str(datetime.now())+"\n\n")
		ff.write(l)
		ff.close()

if __name__ == "__main__":
	tr("Democracy")
