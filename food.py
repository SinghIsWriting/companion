from colorama import Fore, init
init(autoreset=True)
from pandas import read_html
from path import path

def diet():
	print(f"{Fore.CYAN}\nTable of Recommended Daily Intakes for Each Nutrient: ")
	print(f"{Fore.CYAN}This table is for an adult male, average weight of 70kg and height of 70inches (177cm).\n")
	print(f"{Fore.YELLOW}RDI - Reference Daily Intake\nDV - Daily Value\nUL - Upper Limit\nDRI - Dietry Reference Intake\n")
	try:
		d = read_html("https://www.myfooddata.com/articles/recommended-daily-intakes.php#recommended-intakes-table")[0].fillna("0")
		blankIndex=[''] * len(d)
		d.index=blankIndex
		print(f"{Fore.YELLOW}Macronutrients: \n", d.iloc[1:10,[0,1,2]])
		print(f"{Fore.YELLOW}Vitamins: \n", d.iloc[12:23,[0,1,2,3]])
		print(f"{Fore.YELLOW}Minerals: \n", d.iloc[29:39,[0,1,2,3]])
	except:
		print(f"{Fore.RED}Opps, something went wrong.")

t = '''Usage: Speak - Nutrition of/in dairy/oils/fats/meat/seafood/vegetable/fruit/bread/grains/soup/nuts/seeds/alcohol products.
'''

def nutri(f):
	print(f"{Fore.CYAN}\nThis table is compiled from United States Dept. of Agriculture (USDA) sources. Included for each food is its weight in grams.")
	print(f'{Fore.YELLOW}In the Measure column, "t" = teaspoon and "T" = tablespoon. In the food nutrient columns, the letter "t" indicates that only a trace amount is available.\n')
	try:
		d = read_html("https://en.m.wikipedia.org/wiki/Table_of_food_nutrients")
		if "dairy" in f:
			int(d[0].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "oils" in f or "fats" in f:
			print(d[1].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "meat" in f:
			print(d[2].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "fish" in f or "sea food" in f:
			print(d[3].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "vegetable" in f:
			print(d[4].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
			print(d[5].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
			print(d[6].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "fruit" in f:
			print(d[7].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
			print(d[8].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
			print(d[9].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "bread" in f or " grains" in f or "biscuit" in f or "pizza" in f or " cakes" in f:
			print(d[10].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
			print(d[11].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "soup" in f:
			print(d[12].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "desserts" in f or "sweets" in f:
			print(d[13].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "nuts" in f or "seeds" in f:
			print(d[14].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		elif "alcohol" in f or "wines" in f or "beverages" in f:
			print(d[15].iloc[:,[0,2,3,4,5,6,7,8]].fillna(" "), "\n")
		else:
			print(f"{Fore.RED}"+t)
	except:
		print(f"{Fore.RED}Opps, something went wrong.")

if __name__ == "__main__":
	diet()
	nutri("alcohol")
