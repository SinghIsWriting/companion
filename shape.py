from time import sleep
from colorama import Fore, init
init(autoreset=True)

def lov():
	for i in range(6):
		for j in range(7):
			if (i == 0 and j%3 != 0):
				print(f"{Fore.RED}s",end="")
			elif (i ==1 and j == 3):
				print(f"{Fore.RED}A",end="")
			elif (i == 1 and j%3 == 0):
				print(f"{Fore.RED}S",end="")
			elif (i-j ==2) or (i+j == 8):
				print(f"{Fore.RED}S",end="")
			else:
				print(" ",end="")
		print()
	print()

def shp():
	for i in range(3):
		sleep(2)
		if i == 1:
			for i in range(6):
				for j in range(7):
					if (i == 0 and j%3 != 0):
						print("s",end="")
					elif (i ==1 and j == 3):
						print("A",end="")
					elif (i == 1 and j%3 == 0):
						print("S",end="")
					elif (i-j ==2) or (i+j == 8):
						print("S",end="")
					else:
						print(" ",end="")
				print()
			print()
		else:
			lov()
		sleep(2)
	print("Visit:", f"{Fore.GREEN}https://github.com/SinghIsWriting/\n")

if __name__ == "__main__":
	shp()
