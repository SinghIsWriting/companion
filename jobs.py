from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path
from requests import get
from csv import reader

url = "https://www.indgovtjobs.in/2015/10/Government-Jobs.html?m=1"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
		d = read_html(url)
		d[1].to_csv(path+"csv/latest_govt_jobs.csv")
else:
	print(f"{Fore.RED}:( Internet connectivity not found!\n")

data = []
with open(path+"csv/latest_govt_jobs.csv", mode="r", encoding="utf-8") as file:
	csvFile = reader(file)
	for lines in csvFile:
		data.append(lines)

def table():
	print(f"{Fore.CYAN}\nLatest govt jobs:")
	i = 0
	data1 = data[:50]
	for rows in data1:
		for j in range(4):
			if j==3:
				print(f"{data1[i][j]}", end="  ")
			if j==2:
				print(f"{data1[i][j]:12}", end="  ")
			elif j==1:
				print(f"{data1[i][j]:50}", end="  ")
			elif j==0:
				print(f"{data1[i][j]:>2}", end="  ")
		i += 1
		print()
	print()

if __name__ == "__main__":
	table()

