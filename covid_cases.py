from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path

url = "https://www.nytimes.com/interactive/2021/world/india-covid-cases.html"

d = read_html(url)

d[1].iloc[:,[0,1,2,4,5]].to_csv(path+"csv/current_covid_cases_deaths_india.csv")

def table():
	print(f"{Fore.CYAN}\nCoronavirus in India - The NewYork Times\n")
	print(d[1].iloc[:,[0,1,2,4,5]])

if __name__ == "__main__":
	table()

