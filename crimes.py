from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path
from speak import speak
from requests import get
from csv import reader

url = "https://en.m.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_crime_rate"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
        d = read_html(url)
        list = d[2][['State / UT','Murder','Rape','Kidnapping']]
        list.to_csv(path+"csv/current_crime_rates.csv")
        d[2].iloc[0:38,[0,4]].to_csv(path+"csv/current_crime_rates.csv", mode='a')
else:
	print(f"{Fore.RED}:( Internet connectivity not found!\n")

data = []
with open(path+"csv/current_crime_rates.csv", mode="r", encoding="utf-8") as file:
	csvFile = reader(file)
	for lines in csvFile:
		data.append(lines)

def table():
        print(f"\n{Fore.CYAN}Crime rate (per 100,000 population) head-wise 2021\n")
        i = 0
        d = data.copy()
        data1 = data[:40]
        for rows in data1:
        	for j in range(5):
        		if j==4:
        			print(f"{data1[i][j]}", end="  ")
        		if j==3:
        			print(f"{data1[i][j]:>4}", end="  ")
        		if j==2:
        			print(f"{data1[i][j]:>4}", end="  ")
        		elif j==1:
        			print(f"{data1[i][j]:24}", end="  ")
        		elif j==0:
        			print(f"{data1[i][j]:>2}", end="  ")
        	i += 1
        	print()
        print()

def search(pm2):
        pm1 = str(pm2).replace("Crime Rate","")
        pm12 = pm1.replace(" Of ","")
        pm = pm12.replace(" In ","").strip()

        i = 0
        for rows in data:
        	nation = data[i][1]
        	if nation == pm:
        		result = data[i][2]
        		print(f"{Fore.CYAN}Crime rate of", pm, f"{Fore.CYAN}per 100,000 population is following. \nMurder cases are", data[i][2],  f"\n{Fore.CYAN}Rape cases are", data[i][3], f"{Fore.CYAN}\nKidnapping cases are", data[i][4])
        		speak(f"Crime rate of {pm} per 100,000 population is following.  Murder cases are {data[i][2]},  Rape cases are {data[i][3]} and Kidnapping cases are {data[i][4]}", "crimes.mp3")
        		break
        	i += 1

if __name__ == "__main__":
        search("Crime Rate In Jammu and Kashmir")
        table()
