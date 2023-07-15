from colorama import Fore, init
init(autoreset=True)
from os import system

apl = {
	"facebook":"start https://m.facebook.com/",
	"youtube":"start https://www.youtube.com/",
	"instagram":"start https://www.instagram.com/",
	"google":"start https://www.google.com/",
	"github":"start https://www.github.com/",
	"bing":"start https://www.bing.com/",
	"whatsapp":"start https://whatsapp.com/",
	"telegram":"start https://telegram.me/",
	"file explorer":"start explorer",
	"windows explorer":"start explorer",
	"edge":"start msedge",
	"chrome":"start chrome",
	"media player":"start wmplayer",
	"notepad":"start notepad",
	"notepad plus plus":"start notepad++",
	"command prompt":"start cmd",
	"vs code":"start code",
	"powershell":"start pwsh",
}

def sysapp(app):
	print(f"{Fore.CYAN}\nList of apps you can open from here: Just say ( open [APP name])")
	try:
		for i in apl.keys():
			print(i.title())
		print()
		system(f"{apl[app]}")
	except:
		pass

if __name__ == "__main__":
	sysapp("youtube")
