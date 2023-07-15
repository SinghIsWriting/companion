from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path
from requests import get
from csv import reader

url = "https://www.91mobiles.com/latest-mobiles-in-india"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
        d = read_html(url)
        d[10].to_csv(path+"csv/new_launched_phones.csv")
else:
	print(f"{Fore.RED}:( Internet connectivity not found!\n")

data = []
with open(path+"csv/new_launched_phones.csv", mode="r", encoding="utf-8") as file:
	csvFile = reader(file)
	for lines in csvFile:
		data.append(lines)

def table():
	print(f"{Fore.CYAN}\nLatest Mobile Phones in India: ")
	i = 0
	for rows in data:
		for j in range(3):
			if j==2:
				print(f"{data[i][j]}", end="  ")
			elif j==1:
				print(f"{data[i][j]:25}", end="  ")
			elif j==0:
				print(f"{data[i][j]:>2}", end="  ")
		i += 1
		print()
	print()

if __name__ == "__main__":
	table()

