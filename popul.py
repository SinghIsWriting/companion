from colorama import Fore, init
init(autoreset=True)
from time import sleep
from pandas import read_html
from path import path
from speak import speak
from requests import get
from csv import reader

url = "https://www.worldometers.info/world-population/"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
        d = read_html(url)
        list = d[4][['Country (or dependency)','Population (2020)','World Share']]
        list.to_csv(path+"csv/current_population.csv")
else:
	print(f"{Fore.RED}:( Internet connectivity not found!\n")


def table():
        print()
        data = []
        with open(path+"csv/current_population.csv", mode="r", encoding="utf-8") as file:
        	csvFile = reader(file)
        	for lines in csvFile:
        		data.append(lines)
        i = 0
        for rows in data:
        	for j in range(4):
        		if j==3:
        			print(f"{data[i][j]}", end="  ")
        		if j==2:
        			print(f"{data[i][j]:18}", end="  ")
        		elif j==1:
        			print(f"{data[i][j]:25}", end="  ")
        		elif j==0:
        			print(f"{data[i][j]:>3}", end="  ")
        	i += 1
        	print()
        print()

def search(pm2):
        pm1 = str(pm2).replace("Population","")
        pm12 = pm1.replace(" Of ","")
        pm = pm12.replace("Country","").strip()
        data = []
        with open(path+"csv/current_population.csv", mode="r", encoding="utf-8") as file:
        	csvFile = reader(file)
        	for lines in csvFile:
        		data.append(lines)
        i = 0
        for rows in data:
        	nation = data[i][1]
        	if nation == pm:
        		result = data[i][2]
        		print(f"{Fore.CYAN}\nPopulation of {pm} is",result)
        		try:
        			speak(f"Population of {pm} is {result}", "Population.mp3")
        		except:
        			pass
        		break
        	i += 1

if __name__ == "__main__":
        search("India")
        table()
