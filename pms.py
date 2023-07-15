from colorama import Fore, init
init(autoreset=True)
from time import sleep
from pandas import read_html
from path import path
from speak import speak
from requests import get
from csv import reader

url = "https://en.m.wikipedia.org/wiki/List_of_current_prime_ministers_by_date_of_assumption_of_office"
url1 = "https://en.m.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
	df_list = read_html(url)
	df_list1 = read_html(url1)
	df_list[0].to_csv(path+"csv/current_prime_ministers.csv")
	df_list1[1].to_csv(path+"csv/current_presidents.csv")
else:
	print(f"{Fore.RED}\n:( Internet connectivity not found! This is last updated offline data\n")

def read(path):
	data = []
	with open(path, mode="r", encoding="utf-8") as file:
		csvFile = reader(file)
		for lines in csvFile:
			data.append(lines)
	i = 0
	for rows in data:
		for j in range(3):
			if j==2:
				print(f"{data[i][j]}", end="  ")
			elif j==1:
				print(f"{data[i][j]:>44}", end=" : ")
			else:
				print(f"{data[i][j]:>3}", end=" ")
		i += 1
		print()

def table():
	read(path+"csv/current_prime_ministers.csv")

def table1():
	read(path+"csv/current_presidents.csv")

def search1(p):
	p1 = str(p).replace("President","")
	p12 = p1.replace(" Of ","")
	pm = p12.replace("Country","").strip()
	
	data = []
	with open(path+"csv/current_presidents.csv", mode="r", encoding="utf-8") as file:
		csvFile = reader(file)
		for lines in csvFile:
			data.append(lines)
	i = 0
	for rows in data:
		nation = data[i][1]
		if nation == pm:
			result = data[i][2]
			print(f"{Fore.CYAN}Head of state {pm} is",result)
			try:
				speak(f"Head of state {pm} is {result}", "Presidents.mp3")
			except:
				pass
			break
		i += 1

def search(pm2):
	pm1 = str(pm2).replace("Prime Minister","")
	pm12 = pm1.replace(" Of ","")
	pm = pm12.replace("Country","").strip()

	data = []
	with open(path+"csv/current_prime_ministers.csv", mode="r", encoding="utf-8") as file:
		csvFile = reader(file)
		for lines in csvFile:
			data.append(lines)
	i = 0
	for rows in data:
		nation = data[i][2].split("of")[-1].strip()
		if nation == pm:
			result = data[i][1]
			print(f"{Fore.CYAN}Prime Minister of {pm} is",result)
			try:
				speak(f"Prime Minister of {pm} is {result}", "PMs.mp3")
			except:
				pass
			break
		i += 1	

if __name__ == "__main__":
	search("Prime Minister Of India")
	search1("President Of India")
	table()

