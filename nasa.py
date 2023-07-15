from colorama import Fore, init
init(autoreset=True)
from requests import get
import os
from PIL import Image
from path import path
from speak import speak

# Include your own API Key here, visit https://api.nasa.gov/ to get API Key
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

Url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

def nasa(date):
	z = date.replace("nasa","").strip()
	Date = z.replace(" ","-")
	print(Date)
	try:
		Paramas = {'date':str(Date)}
		r = get(Url,params = Paramas)
		Data = r.json()
		Title = Data['title']
		Info = Data['explanation']
		image = Data['url']
		image_r = get(image)
		fn = str(Title)+str(Date)+".png"
		with open(fn,'wb') as f:
			f.write(image_r.content)
			f.close()
		print(f"{Fore.CYAN}Title:",Title)
		print(f"{Fore.CYAN}According to Nasa:")
		print(Info)
		try:
			path1 = path+str(fn)
			path2 = path+"nasaImages/"+str(fn)
			os.rename(path1, path2)
		except:
			pass
		
		t = f"This update is about {Title}"
		speak(t, "NasaTitle.mp3")
		img = Image.open(path2)
		img.show()
		speak(Info, "Nasa.mp3")
	except:
		print(f"{Fore.YELLOW}Usage: speak - nasa yyyy-mm-dd OR nasa today\n")
if __name__ == "__main__":
	nasa("nasa")
