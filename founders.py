from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path
from requests import get
from csv import reader

url = "https://cracku.in/blog/list-of-top-companies-and-their-ceos-in-world-pdf/"
url1 = "https://eduhyme.com/world-major-companies-their-founders/"
url2 = "https://en.m.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
url3 = "https://en.m.wikipedia.org/wiki/Fortune_Global_500"

req = ""
try:
	req = str(get("https://www.google.com/"))
except:
	pass
if req == "<Response [200]>":
        d = read_html(url)
        d1 = read_html(url1)
        d2 = read_html(url2)
        d3 = read_html(url3)

        d[0].iloc[:,[1,2,3]].to_csv(path+"csv/companies_ceos.csv")
        d1[0].iloc[:,[1,2]].to_csv(path+"csv/companies_founders.csv")
        d2[0].iloc[:,[0,1,2,3]].to_csv(path+"csv/companies_revenue.csv")
        d3[1].iloc[:,[0,1,2]].to_csv(path+"csv/companies_numbers_in_countries.csv")
else:
	print(f"{Fore.RED}\n:( Internet connectivity not found! This is last updated offline data\n")

def table():
        print(f"{Fore.CYAN}\nCompanies, headquarters and thier CEOs:")
        data = []
        with open(path+"csv/companies_ceos.csv", mode="r", encoding="utf-8") as file:
                csvFile = reader(file)
                for lines in csvFile:
                        data.append(lines)
        print(f"{Fore.CYAN}No. of Companies:",len(data)-1)
        i = 0
        for rows in data:
                for j in range(4):
                        if j==3:
                                print(f"{data[i][j]}", end="  ")
                        elif j==2:
                                print(f"{data[i][j]:40}", end="  ")
                        elif j==1:
                                print(f"{data[i][j]:32}", end="  ")
                        else:
                                print(f"{data[i][j]}", end="  ")
                i += 1
                print()
        print(f"{Fore.CYAN}No. of Companies: {len(data)-1}\n")

def table1():
        print(f"{Fore.CYAN}\nCompanies and thier founders:")
        data = []
        with open(path+"csv/companies_founders.csv", mode="r", encoding="utf-8") as file:
        	csvFile = reader(file)
        	for lines in csvFile:
        		data.append(lines)
        i = 0
        for rows in data:
        	for j in range(3):
        		if j==2:
        			print(f"{data[i][j]}", end=" ")
        		elif j==1:
        			print(f"{data[i][j]:>20}", end=" : ")
        		else:
        			print(f"{data[i][j]}", end=" ")
        	i += 1
        	print()
        print()

def table2():
        data = []
        with open(path+"csv/companies_revenue.csv", mode="r", encoding="utf-8") as file:
        	csvFile = reader(file)
        	for lines in csvFile:
        		data.append(lines)
        print(f"{Fore.CYAN}\nThese are top {len(data)-1} Companies in the world.")
        print(f"{Fore.CYAN}\nCompanies and thier Revenue:")
        i = 0
        for rows in data:
        	for j in range(1,5):
        		if j==4:
        			print(f"{data[i][j]}", end=" ")
        		if j==3:
        			print(f"{data[i][j]:22}", end="  ")
        		elif j==2:
        			print(f"{data[i][j]:40}", end="  ")
        		elif j==1:
        			print(f"{data[i][j]:>4}", end=" ")
        	i += 1
        	print()
        print()

def table3():
        print(f"{Fore.CYAN}\nCountries with number of companies:")
        data = []
        with open(path+"csv/companies_numbers_in_countries.csv", mode="r", encoding="utf-8") as file:
        	csvFile = reader(file)
        	for lines in csvFile:
        		data.append(lines)
        i = 0
        for rows in data:
        	for j in range(1,4):
        		if j==3:
        			print(f"{data[i][j]}", end="  ")
        		if j==2:
        			print(f"{data[i][j]:15}", end="  ")
        		elif j==1:
        			print(f"{data[i][j]:>4}", end="  ")
        	i += 1
        	print()
        print()

if __name__ == "__main__":
        table()
        table1()
        table2()
        table3()
