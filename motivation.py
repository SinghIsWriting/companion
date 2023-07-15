from colorama import Fore, init
init(autoreset=True)
from requests import get
from bs4 import BeautifulSoup
from random import choice
from path import path
from speak import speak

url = "https://www.gofugly.in/"

def motiv():
	try:
		d = get(url)
		soup = BeautifulSoup(d.text, "lxml")
		b = soup.find_all("div",class_="col-md-3 col-sm-3")
		t = soup.find_all("a", class_="btn-default")
		a = set()
		for i in t:
			a.add(i["title"])
		m = choice(list(a))
		print(f"\n{Fore.YELLOW}Quotes:",m)
		print()
		speak(m, "motivation.mp3")
	except:
		pass

if __name__ == "__main__":
	motiv()
