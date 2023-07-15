from requests import get
import json
from colorama import Fore, init
init(autoreset=True)
from path import path
from speak import speak

# Include your own News API key, to do the same you can visit https://newsapi.org/
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def get_news(cat):
	url = f'https://newsapi.org/v2/top-headlines?country=in&category={cat}&apiKey={API_KEY}'
	try:
		news = get(url).text
		news_dict = json.loads(news)
		articles = news_dict['articles']
		title = []
		urls = []
		title_url = []
		for index, articles in enumerate(articles):
			d = articles['publishedAt']
			title.append(articles['title'])
			urls.append(articles['url'])
			title_url.append("\n"+articles['title']+"\n"+articles['url'])
		e = f"{cat.title()} news\nThis news was published in "+d[0:10]
		g = d[0:10]
		s = '\n'.join(title_url[0:5])
		title_url.insert(0, e)
		print(e)
		for i in range(5):
			print(f"[{i+1}]",title[i])
			print(f"{Fore.BLUE}"+urls[i])
		s1 = f"These Headlines were punlished on {g}"+'\n'.join(title[0:5])
		with open(path+"txt/newsHeadlines.txt","a", encoding="utf-8") as f:
			f.write(e)
			f.writelines(s)
			f.write(d)
			f.write("\n")
			f.write("*"*70)
			f.write("\n\n")
		speak(s1, "news.mp3")
		print("\n[#] For more info about headlines visit the url given below them. \n\nYou can get news about these category:\n[1] Science   [2] Business   [3] Technology\n[4] Health    [5] Sport      [6] Entertainment\n")
	except:
		print(f"{Fore.RED}\nOpps, something went wrong!")
		print(f"{Fore.YELLOW}Usage: speak NEWS_CATEGORY news\n")

if __name__ == "__main__":
	get_news("science")
