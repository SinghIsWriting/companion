from colorama import Fore, init
init(autoreset=True)
from os import system

def show():
	system(f"ipconfig > ip.txt")
	with open("ip.txt","r", encoding="utf-8") as s:
		l = s.read().strip()
	ip = ((l.split("Wi-Fi"))[-1]).split("192")
	print(f"{Fore.YELLOW}Your device IP:", "192"+ip[1][0:12])

if __name__ == "__main__":
	show()

