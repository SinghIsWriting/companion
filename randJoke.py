from colorama import Fore, init
init(autoreset=True)
from requests import get
from path import path
from speak import speak

def jok():
	url = "http://official-joke-api.appspot.com/random_joke"
	data = get(url).json()
	print(f"{Fore.CYAN}"+data['setup'])
	print(f"{Fore.CYAN}"+data['punchline'])
	l = data['setup']+"\n"+data['punchline']
	speak(l, "jokes.mp3")

if __name__ == "__main__":
	jok()
