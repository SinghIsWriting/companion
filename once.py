from datetime import datetime
from os import system
from time import sleep
from speak import speak
from colorama import Fore, init
init(autoreset=True)
from requests import get

hr = str(datetime.now().hour)
starting = ['Initializing program',
		'Caliberating and examining all the core processes',
		'Checking the internet connection',
		'Caliberating and examining all the core processes',
		'Wait a moment sir',
		'System has been activated now']

def inits():
	for s in starting:
		speak(f"{s}", "hello.mp3")
		if starting.index(s) == 0 or starting.index(s) == 2 or starting.index(s) == 5:
			if starting.index(s) == 2:
				req = ""
				try:
					req = str(get("https://www.google.com/"))
				except:
					pass
				if req == "<Response [200]>":
					pass
				else:
					print("Checking the internet connection...")
					sleep(1)
					print(f"{Fore.RED}:( Internet connectivity not found!\n")
					break
		print(s+"...",end=" ")
		sleep(1)
		print("✅ done")
		sleep(1)
    print('\nNow please tell me how may I help you')

if __name__ == "__main__":
	inits()
