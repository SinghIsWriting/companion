from playsound import playsound
from gtts import gTTS
from path import path
from colorama import Fore, init
init(autoreset=True)

def speak(audio, file="file.mp3", lang="en"):
    try:
        words = gTTS(audio, lang=lang)
        words.save(path+"mp3/"+file)
        playsound(path+"mp3/"+file)
    except:
        pass
    
l = '''Create a computational graph By creating computational graph, we mean defining the nodes.'''

if __name__ == "__main__":
    speak(l)
