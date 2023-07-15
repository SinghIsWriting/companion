from colorama import Fore, init
init(autoreset=True)
from datetime import datetime
from requests import get
from path import path
from speak import speak

# Include your own NASA open API key here, visit https://api.nasa.gov/
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Definig a function that takes start and ending dates primarily and extract asteroid information from the NASA website
def astro():
	start_date = datetime.now().strftime("%Y-%m-%d")
	end_date = datetime.now().strftime("%Y-%m-%d")

	url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

	r = get(url)
	Data = r.json()    # Data json found about asteroids
	try:
		# Extracting info from data json
		total_astroids = Data['element_count']
		close_objects = Data['near_earth_objects']
		print(f"{Fore.YELLOW}\nTotal number of astroids:",total_astroids)
		danger = []
		toSpeak = ""
		for body in close_objects[start_date]:
			id = body['id']
			name = body['name']
			mag = body['absolute_magnitude_h']
			dia = str(body['estimated_diameter']['kilometers']['estimated_diameter_min'])+" - "+str(body['estimated_diameter']['kilometers']['estimated_diameter_min'])+" kilometers"
			haz = body['is_potentially_hazardous_asteroid']
			vel = str(body['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])+" km/hrs"
			orbit = body['close_approach_data'][0]['orbiting_body']
			missd = str(body['close_approach_data'][0]['miss_distance']['miles'])+" miles"
			aptime = body['close_approach_data'][0]['close_approach_date_full']

			magnitude = "Magnitude"
			diameter = "Diameter"
			potential = "Potential Hazardous?"
			velocity = "Relative Velocity"
			orbBody = "Orbiting Body"
			missingDistance = "Missing Distance"

			print(f"{Fore.GREEN}Id:", (id),
				f"{Fore.GREEN}Name:", (name),
				f"{Fore.CYAN}\n\t{magnitude:>25} :", (mag),
				f"{Fore.CYAN}\n\t{diameter:>25} :", (dia),
				f"{Fore.CYAN}\n\t{potential:>25} :", (haz),
				f"{Fore.CYAN}\n\t{velocity:>25} :", (vel),
				f"{Fore.CYAN}\n\t{orbBody:>25} :", (orbit),
				f"{Fore.CYAN}\n\t{missingDistance:>25} :", (missd),
				f"{Fore.CYAN}\n\t Approaching to the Earth :", (aptime))
			print()
		danger.append(str(body['close_approach_data'][0]['miss_distance']['miles']))
		toSpeak = f"There are {total_astroids} asteoids near the Earth today. "+f"The closest astroid approaching to earth is {round(float(min(danger)), 3)} miles away from our earth."
		print(f"{Fore.RED}The Closest approaching astroid is",min(danger),f"{Fore.RED}miles away from earth.")
		print(f"{Fore.GREEN}Total number of astroids near the earth:", total_astroids)
		print()
		speak(toSpeak, "astro.mp3")
	except:
		print(f"{Fore.YELLOW}\nWARNING: Opps, something went wrong!")

if __name__ == "__main__":
	astro()

