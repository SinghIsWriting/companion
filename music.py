from colorama import Fore, init
init(autoreset=True)
from playsound import playsound
from random import choice
from speak import speak
from path import path

songs = [
	"Love Me Like You Do_320.mp3",
	"I Am So Obsessed_320.mp3", 
	"brokenAngel.mp3",
]

def mL(r):
	if r == '':
		playsound(path+"mp3/"+choice(songs))
	elif 'romantic ' in r:
		playsound(f"{path}Love Me Like You Do_320(PagalWorld.com.se).mp3")
	elif 'sad ' in r:
		playsound(f"{path}I Am So Obsessed_320(PagalWorld).mp3")
	elif 'broken ' in r:
		playsound(f"{path}brokenAngel.mp3")
	else:
		try:
			speak("Playing the song on Spotify")
			from spotAlbums import spot
			spot(r)
		except:
			print("\nOpps, something went wrong.\n")

def song():
	print(f"{Fore.GREEN}\nThese three songs are default songs")
	for i in range(len(songs)):
		print(f"[{i+1}] ",f"{Fore.YELLOW}"+songs[i])
	print(f'{Fore.CYAN}\nYou can play songs on Spotify and play some downloaded songs. Just say "Play [SONG NAME]".\n')
	speak("You can play songs on Spotify and play some default songs. Just say Play SONG NAME", "hello.mp3")
if __name__ == "__main__":
	# mL("Song")
	song()
