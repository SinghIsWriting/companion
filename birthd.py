from colorama import Fore, init
init(autoreset=True)
from csv import reader
from datetime import datetime
from path import path

fo = open(path+"csv/bdays.csv", "r", encoding="utf-8")
content = reader(fo, delimiter =",")

dy = datetime.now().day
mon = datetime.now().month

for each in content:
	if str(mon) == each[1] and str(dy) == each[2]:
		print(f"{Fore.YELLOW}🎂🎉🎊 It's"+f"{Fore.YELLOW} {each[0]}"+f"{Fore.YELLOW}'s birthday today!!")
	else:
		pass
fo.close()

if __name__ == "__main__":
	print(dy,mon)

