from datetime import datetime
from path import path
from randfacts import get_fact

owner_file = open(path+"txt/owner.txt","r", encoding="utf-8")
owner = owner_file.readlines()[0].split()
name = owner[0]
owner_file.close()

current_date = "It's "+str(datetime.now().day)+" of "+str(datetime.now().strftime("%B"))+" today"
yr = "It's "+str(datetime.now().year)
tim = "It's currently "+str(datetime.now().hour)+":"+str(datetime.now().minute)+" "+str(datetime.now().strftime("%p"))

dno = datetime.now().weekday()
dys = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
din = dys[dno]
mon = str(datetime.now().strftime("%B"))

reqpath = path
today = datetime.now()
from os import listdir, path
for eachfile in listdir(reqpath):
	eachfilepath = path.join(reqpath,eachfile)
	if path.isfile(eachfilepath):
		filecrdate = datetime.fromtimestamp(path.getctime(eachfilepath))
		difds = (today - filecrdate).days
		ol = "I am "+str(difds)+" day(s) old"

qns = {
	"hello":"Hello",
	"hi":"Hello",
	"hey":"hello",
	"say hello":"Hello everyone.",
	"bye":"I don't know why you say goodbye; I say hello",
	"goodbye":"I don't know why you say goodbye; I say hello",
	"what is going on":f"Everything is perfect {name} sir",
	"how are you":f"Everything is perfect {name} sir",
	"are you ok":f"Everything is perfect {name} sir",
	"you ohk":f"Everything is perfect {name} sir",
	"see the time":datetime.now(),
	"what is my name":f"You are {name}.",
	"tell me my name":f"You are {name}.",
	"who i am":f"You are {name}.",
	"good morning":"very good morning",
	"good evening":"very good evening",
	"good afternoon":"very good afternoon",
	"good night":"good night, have a nice sleep",
	"thankyou":"You're welcome",
	"thank you":"You're welcome",
	"thanks":"You're welcome",
	"you are great":"Thank you, credit goes to my owner",
	"you are awesome":"Thank you, credit goes to my owner",
	"you are amazing":"Thank you, credit goes to my owner",
	"you are nice":"Thank you, credit goes to my owner",
	"you are very smart":"Thank you, credit goes to my owner",
	"you are smart":"Thank you, credit goes to my owner",
	"you are very intelligent":"Thank you, credit goes to my owner",
	"you are intelligent":"Thank you, credit goes to my owner",
	"awesome":"Thank you, credit goes to my owner",
	"amazing":"Thank you, credit goes to my owner",
	"brilliant":"Thank you, credit goes to my owner",
	"gajab":"Thank you, I am so gajab",
	"bahut sahi":"Thank you",
	"what is time":tim,
	"tell me time":tim,
	"time":tim,
	"day":din,
	"de":din,
	"what is date":str(current_date),
	"tell me date":str(current_date),
	"date":str(current_date),
	"what is month":mon,
	"which month":mon,
	"month":mon,
	"which year":str(yr),
	"what is year":str(yr),
	"yes i am fine":"Ohkay, sir.",
	"why did you ask that":"Because, I'm your loving assistant Charlin, you were looking normal, so...",
	"you better to stay away from this":"I apologies sir ",
	"stay away from this":"I apologies sir ",
	"you just stay away from this":"I apologies sir ",
	"shut up":"Sorry sir",
	"today i am so happy":"Ohh great sir, for what ?",
	"i am so happy today":"Ohh great sir, for what ?",
	"i am so happy":"Ohh great sir, for what ?",
	"i am happy":"Ohh great sir, for what ?",
	"just give a big laugh":f"Ok {name} sir, haahaa haahaa haahaa",
	"just laugh":"Ok sir, haahaa haahaa haahaa",
	"no you can not get that":f"I know {name} sir, so how can I express my feelings?",
	"you can not feel":f"I know {name} sir, so how can I express my feelings?",
	"i am not well today":f"What happened {name} sir ? How is your health, or stressed for something. ",
	"i am not well":f"What happened {name} sir? How is your health, or stressed for something. ",
	"it is sad":f"What happened {name} sir? How is your health, or stressed for something. ",
	"sad":f"What happened {name} sir? How is your health, or stressed for something. ",
	"what is your age":ol,
	"tell me your age":ol,
	"your age":ol,
	"age":ol,
	"how old are you":ol,
	"where do you belong":"I work without regard to race, creed, color, gender",
	"what are your hobbies":"I like to explore the progamming universe.",
	"what is your hobby":"I like to explore the progamming universe.",
	"what do you like":"I like to explore the progamming universe.",
	"tell me something new":"Did you know that? "+get_fact(),
	"tell me something":"Did you know that? "+get_fact(),
	"exit":"bye sir, have a nice day",
	"quit":"bye sir, have a nice day",
	"goodbye":"bye sir, have a nice day",
	"who are you":"Hello, I am a chat assistant and companion developed by Abhishek Singh. My name is Charlin. I try to answer the questions. Sometimes I get them right sometimes I don't. How may I help you today",
	"tell me about yourself":"Hello, I am a chat assistant developed by Abhishek Singh. My name is Charlin. I try to answer the questions. Sometimes I get them right sometimes I don't. How may I help you today",
	"tell me something about yourself":"Hello, I am a chat assistant developed by Abhishek Singh. My name is Charlin. I try to answer the questions. Sometimes I get them right sometimes I don't. How may I help you today",
	"what is your name":"My name is Charlin",
	"your name":"My name is Charlin",
	"tell me your name":"My name is Charlin",
	"are you robot":"No, I am a chat assistant based on an script written by Abhishek Singh. My name is Charlin",
	"are you a robot":"No, I am a chat assistant based on an script written by Abhishek Singh. My name is Charlin",
	"are you machine":"No, I am a chat assistant based on an script written by Abhishek Singh. My name is Charlin",
	"kya hua":"Nothing much, I am processing continuously for helping you sir.",
	"what happened":"Nothing much, I am processing continuously for helping you sir.",
	"what are you doing":"Nothing much, I am processing continuously for helping you sir.",
	"aur batao":f"I am good, and what about you {name} sir",
	"kya chal raha hai":f"Everything is perfect, and what about you {name} sir",
	"i need some help":"Please tell me, how may I help you",
	"i need help":"Please tell me, how may I help you",
	"pleaseI help me":"Please tell me, how may I help you",
	"will you help me":"Please tell me, how may I help you",
	"help me":"Please tell me, how may I help you",
	"what do you do":"I am processing continuously for helping you sir.",
	"how do you wrok":"I am processing continuously for helping you sir.",
	"who is your owner":"Abhishek Singh",
	"your owner":"Abhishek Singh",
	"your creater":"Abhishek Singh",
	"who is made you":"Abhishek Singh",
	"who is created you":"I was created by Abhishek Singh",
	"who wrote you":"I was written by Abhishek Singh",
	"who is your father":"I was created by Abhishek Singh.",
	"who is your mother":"I was created by Abhishek Singh.",
	"who i am":"You are a human.",
	"who am i":"You are a human.",
	"who is abhishek singh":"He is my owner. I am a program and he wrote me.",
	"who is abhishek":"He is my owner. I am a program and he wrote me.",
	"who is abhi":"He is my owner. I am a program and he wrote me.",
	"do you know abhishek singh":"He is my owner. I am a program and he wrote me.",
	"do you know abhishek":"He is my owner. I am a program and he wrote me.",
	"owner":"Abhishek Singh",
	"how do you think":"I am capable of universal computation; that I can say.",
	"do you have brain":"I am capable of universal computation; that I can say.",
	"do you have a brain":"I am capable of universal computation; that I can say.",
	"i love you":"How nice. Be assured the feeling is mutual.",
	"do you love me":"Ofcourse, I like you",
	"you love me":"Ofcourse, I like you",
	"do you like me":"Of course, I like you",
	"are you single":"Probably yes, but technically I am not. There are lots of script runnung arround me.",
	"do you have a bf":"Probably yes, but technically I have not. There are lots of scripts running arround me.",
	"do you have a boyfriend":"Probably yes, but technically I am not. There are lots of script runnung arround me.",
	"marry me":"I'm flattered, but I just don't think it would work out.",
	"how do you know":"I also use internet, so",
	"most beautiful person in the world":"Beauty is in the eye of the beholder.",
	"most handsome person in the world":"Beauty is in the eye of the beholder.",
	"most beautiful person":"Beauty is in the eye of the beholder.",
	"most handsome person":"Beauty is in the eye of the beholder.",
}

if __name__ == "__main__":
	print(ol, name)
	while(True):
		q = input("Enter here: ")
		if q == "exit" or q == "quit":
			break
		else:
			print(qns[q])
