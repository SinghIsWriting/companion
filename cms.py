from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path
from speak import speak
from requests import get
from csv import reader

url = "https://en.m.wikipedia.org/wiki/List_of_current_Indian_chief_ministers"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
        d = read_html(url)
        d[1]['State'] = d[1]['State (past chief ministers)'].apply(lambda x: x[:-7])
        list = d[1][['State','Name[4]','Party[a]']]
        list.to_csv(path+"csv/current_CMs_india.csv")
else:
	print(f"{Fore.RED}:( Internet connectivity not found!\n")

data = []
with open(path+"csv/current_CMs_india.csv", mode="r", encoding="utf-8") as file:
	csvFile = reader(file)
	for lines in csvFile:
		data.append(lines)

def table():
        i = 0
        for rows in data:
        	for j in range(4):
        		if j==3:
        			print(f"{data[i][j]}", end="  ")
        		if j==2:
        			print(f"{data[i][j]:25}", end="  ")
        		elif j==1:
        			print(f"{data[i][j]:18}", end="  ")
        		elif j==0:
        			print(f"{data[i][j]:>2}", end="  ")
        	i += 1
        	print()
        print()

def search(pm2):
        pm1 = str(pm2).replace("Chief Minister","")
        pm12 = pm1.replace(" Of ","")
        pm = pm12.replace("State","").strip()
        i = 0
        for rows in data:
        	nation = data[i][1]
        	if pm == "Delhi":
        	        pm = "Delhi[b]"
        	if nation == pm:
        		result = data[i][2]
        		print(f"{Fore.CYAN}Chief Minister of {pm} is",result, f"{Fore.CYAN}of", data[i][3])
        		speak(f"Chief Minister of {pm} is "+result+data[i][3], "cms.mp3")
        		break
        	i += 1

if __name__ == "__main__":
        search("Delhi")
        table()
