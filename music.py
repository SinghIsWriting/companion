from colorama import Fore, init
init(autoreset=True)
from playsound import playsound
from random import choice
from speak import speak
from path import path
from os import listdir

songs_list = listdir(path+"mp3/songs/")

def mL(r):
	if r == '':
		playsound(path+"mp3/songs/"+choice(songs_list))
	elif 'romantic ' in r:
		playsound(f"{path}mp3/songs/Love Me Like You Do_320(PagalWorld.com.se).mp3")
	elif 'sad ' in r:
		playsound(f"{path}mp3/songs/I Am So Obsessed_320(PagalWorld).mp3")
	elif 'broken ' in r:
		playsound(f"{path}mp3/songs/brokenAngel.mp3")
	else:
		try:
			speak("Playing the song on Spotify")
			from spotAlbums import spot
			spot(r)
		except:
			print("\nOpps, something went wrong.\n")

def song():
	print(f"{Fore.GREEN}\nThese three songs are default songs")
	for i in range(len(songs_list)):
		print(f"[{i+1}] ",f"{Fore.YELLOW}"+songs_list[i])
	print(f'{Fore.CYAN}\nYou can play songs on Spotify and play some downloaded songs. Just say "Play [SONG NAME]".\n')
	speak("You can play songs on Spotify and play some default songs. Just say Play SONG NAME", "hello.mp3")
if __name__ == "__main__":
	# mL("Song")
	song()
