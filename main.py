import subprocess
from time import sleep
import speech_recognition as sr
import os
import sys
from datetime import datetime
from colorama import Fore, init
init(autoreset = True)
import birthd
from getpass import getpass
from speak import speak
from webbrowser import open
from path import path

def takeCommand():
    print("\n", f"{Fore.GREEN}-"*107)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, 1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(f"{Fore.GREEN}Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"{Fore.RED}Sorry sir...please repeat it again.", e)
        return "None"
    return query

owner_file = open(path+"txt/owner.txt","r", encoding="utf-8")
owner = owner_file.readlines()[0].split()
name = owner[0]
owner_file.close()

c = False
hr = int(datetime.now().hour)
ti = str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second)

def wish():
	if hr>=0 and hr<12:
		speak(f"Good morning {name} sir", "wish.mp3")
		from once import inits
		inits()
	elif hr>=12 and hr<18:
		speak(f"Good afternoon {name} sir", "wish.mp3")
		from once import inits
		inits()
	else:
		speak(f"Good evening {name} sir", "wish.mp3")
		from once import inits
		inits()

for i in range(3):
	a = getpass("Enter password: ")
	password_file = open(path+"txt/passwd.txt","r", encoding="utf-8")
	password = password_file.readlines()[0].split()
	pw = password[0]
	password_file.close()
	if a==pw:
		try:
			os.system("cls")
		except:
			os.system("clear")
		print(f"{Fore.CYAN}\n:::::::::::::::::::::::::::::::::::::",f"{Fore.GREEN}Welocome to Your True Companion",f"{Fore.CYAN}:::::::::::::::::::::::::::::::::::::\n")
		wish()
		break
	elif (i==2 and a!=pw):
		sys.exit()
	else:
		print("Wrong password ❌,Try Again\n")
import chat

if __name__ == "__main__":
	while True:
		res = takeCommand()
		with open(path+"txt/logs.txt","a", encoding="utf-8") as f:
			if res == "":
				pass
			else:
				f.write(f"{res}    [{datetime.now()}]\n")
			f.close()
		res = res.lower()

		if res == 'system id':
			intro = subprocess.Popen('whoami')
		elif res in chat.qns.keys():
			from speak import speak
			t = chat.qns[res]
			print("Charlin:",f"{Fore.MAGENTA}"+t)
			speak(t)
		elif "weather" in res:
			w = res.replace("weather","")
			w1 = w.replace(" of ","")
			w2 = w1.replace(" in ","").strip()
			import weather
			weather.weath(w2)
		elif res == "bye" or res == "ok bye":
			if hr>=0 and hr<18:
				speak(f"Have a nice day {name}", "hello.mp3")
			elif hr>=18 and hr<21:
				speak(f"Have a pleasant evening {name}", "hello.mp3")
			else:
				speak(f"Good night {name}, sleep well.", "hello.mp3")
			print("\nSee you soon.")
			break
		elif 'stop' in res or 'sleep' in res:
			print(f"{Fore.YELLOW}Sleeping for 60 seconds...")
			sleep(60)
		elif "query" in res or "question" in res:
			import queries
			speak(f"sure {name} sir, please enter your query...", "hello.mp3")
			queries.wolf()
		elif "about" in res:
			import wiki
			wiki.wk(res)
		elif "calendar" in res:
			import cal
			cal.cl(res)
		elif "love" in res:
			import shape
			shape.shp()
		elif ("change" in res and "name" in res) or ("reset" in res and "name" in res):
			name = input("Enter your name: ")
			from jofufa import iname
			iname(name)			
		elif ("play " in res or "sing " in res):
			from music import mL
			if "play " in res:
				qz = res.replace("play ","").strip()
				mL(qz)
			elif "sing " in res:
				qz1 = res.replace("sing ","").strip()
				mL(qz1)
			else:
				print(f"{Fore.YELLOW}Usage: speak - play/sing SONG_NAME\n")
		elif ("display " in res or "list " in res) and ("song " in res or "songs " in res):
			from music import song
			song()
		elif ("covid" in res or "kovid" in res) and "table" in res:
			from covid_cases import table
			table()
		elif "news" in res:
			from news import get_news
			s = res.replace("news","").strip()
			get_news(s)
		elif "translate" in res:
			trs = res.replace("translate","").strip()
			if trs == "":
				pass
			else:
				from langTrans import tr
				tr(trs)
		elif "in english" in res and "translate" in res:
			trs1 = res.replace("in english","").strip()
			trs2 = trs1.replace("translate","").strip()
			from hindiToAllTranslation import tr
			tr(trs2)
		elif "open" in res:
			import systemApp
			zzz = res.replace("open","")
			systemApp.sysapp(zzz.strip())
		elif "search" in res:
			z = res.replace("search","")
			y = z.replace(" ","+")
			os.system("https://google.com/search?q="+y)
		elif "scan my ip" in res:
			try:
				from scan_port import scan
				scan()
			except:
				print(f"{Fore.YELLOW}Usage: speak - scan my IP\n")
		elif "my ip" in res:
			from ipad import show
			show()
		elif "nasa" in res:
			from nasa import nasa
			if "today" in res:
				nasa(str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day))
			else:
				nasa(res)
		elif "asteroid" in res:
			from asteroid import astro
			astro()
		elif "map" in res:
			l = res.replace("map ","")
			m = l.replace(" of ","")
			n = m.replace("show ","")
			o = n.replace("the ","").strip()
			open(f"https://www.google.com/maps/place/{o}")
		elif "movie" in res:
			if " table " in res or " list " in res or "upcoming" in res:
				from new_movies import table
				table()
			else:
				from moviesIMDB import search_movie
				qz = res.replace("movie","").strip()
				search_movie(qz)
		elif "funny" in res:
			from randJoke import jok
			jok()
		elif "joke" in res or "jokes" in res:
			jok = res.replace(res,"joke").strip()
			from jofufa import dic
			koj = dic[jok]
			print("Charlin:",f"{Fore.MAGENTA}"+koj)
			speak(koj)
		elif "fact" in res or "facts" in res:
			fc = res.replace(res,"fact").strip()
			from jofufa import dic
			cf = dic[fc]
			print("Charlin:",f"{Fore.MAGENTA}"+cf)
			speak(cf)
		elif "¥1" in res or "€1" in res or "$1" in res or "rupees" == res or "rs 1" in res or "£1" in res or "one pound" in res or "chinese currency" in res or "japanese currency" in res:
			try:
				from jofufa import dic
				cu = dic[res]
				print("Charlin:",f"{Fore.MAGENTA}"+cu)
				speak(cu)
			except:
				print("Usage: Say [japanese currency/chinese currency/rupees/one pound/¥1/$/€1/£1]")
		elif "btc" in res or "bitcoin" in res:
			from jofufa import dic
			bit = dic['btc']
			print("Charlin:",f"{Fore.MAGENTA}"+bit)
			speak(bit)
		elif "birth" in res and "table" in res:
			from pandas import read_csv
			t = read_csv(path+"csv/bdays.csv")
			print(t)
			speak(f"There a are {len(t)} persons are in your database.", "hello.mp3")
		elif "motivation" in res and "quote" in res:
			from motivation import motiv
			motiv()
		elif ("story" in res or "stories" in res) and ("tell" in res or "show" in res):
			if "inspiration" in res or "inspire" in res or "motivation" in res or "motivate" in res:
				if "hindi" in res:
					from inspStory import hstory
					hstory()
				else:
					from inspStory import story
					story()
			else:
				if "hindi" in res:
					from mythStories import hstory
					hstory()
				else:
					from mythStories import story
					story()
		elif ("diet" in res or "nutrition" in res) and ("list" in res or "table" in res):
			from food import diet
			diet()
		elif "nutrition" in res and (" of " in res or " in " in res):
			from food import nutri
			nutri(res)
		elif ("comapies" in res or "company" in res) and ("table" in res or "list" in res):
			if "founder" in res or "owner" in res:
				from founders import table1
				table1()
			elif "chief officer" or "head quarter" in res or " o " in res or "where" in res:
				from founders import table
				table()
			elif "revenue" in res or "worth" in res or "value" in res:
				from founders import table2
				table2()
			elif "number" in res:
				from founders import table3
				table3()
			else:
				print(f"{Fore.YELLOW}Speak - Companies/company [founder/chief officer/head quarter/revenue/worth/number] table/list \n")
		elif ("prime minister" in res or "president" in res or "population" in res or "chief minister" in res or "crime" in res) and ("table" in res or "list" in res):
			if "president" in res:
				from pms import table1
				table1()
			elif "population" in res:
				from popul import table
				table()
				sleep(5)
				open("https://www.worldometers.info/world-population/")
			elif "chief minister" in res:
				from cms import table
				table()
			elif "crime rate" in res:
				from crimes import table
				table()
			else:
				from pms import table
				table()
		elif ("prime minister " in res or "president" in res or "population" in res or "chief minister" in res or "crime rate" in res) and (" of " in res or " in " in res):
			if "president" in res:
				from pms import search1
				search1(res.title())
			elif "population" in res:
				from popul import search
				search(res.title())
			elif "chief minister" in res:
				from cms import search
				search(res.title())
			elif "crime rate" in res:
				from crimes import search
				search(res.title())
			else:
				from pms import search
				search(res.title())
		elif ("mobile" in res or "job" in res) and (" table" in res or "list" in res):
			if "mobile" in res:
				from mobiles import table
				table()
			elif "job" in res:
				from jobs import table
				table()
			else:
				print(f"{Fore.YELLOW}Speak - Lates mobiles/jobs list/table\n")
		elif res == 'calendar':
			from cal import cl
			cl()
		elif 'files' in res or 'file' in res:
			os.system("tree")
		elif res == 'MD':
			os.mkdir(path+"d1")
			print(os.listdir(path))
		elif res == 'clear screen':
			os.system("cls")
		elif res == 'release':
			rs = input(" Enter the package name: ").lower()
			cmd = [rs,'--version']
			sp = subprocess.Popen(cmd, shell = False,
				universal_newlines = True)
		elif ('write' in res or "make" in res) and "note" in res:
			print("Writting...")
			res = res.replace("write","")
			with open(path+"txt/note.txt","a", encoding="utf-8") as fo:
				fo.writelines(f"{res}  \n{datetime.now()} \n\n")
		else:
			pass

