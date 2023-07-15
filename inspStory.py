from colorama import Fore, init
init(autoreset=True)
from random import choice
from googletrans import Translator
from path import path
from speak import speak

s1 = '''The Dedication of Ekalavya
Ekalavya was a young boy living with his tribe, deep in the forest. His aim in life was to become the finest archer the world had ever seen. However, when he asked to become Drona’s student, he was refused, due to the low status of his birth. Despite this, Ekalavya created a statue of Drona and practised archery before it, until he became incredibly skilled. However, when Drona encountered him and learned of his accomplishments, he was afraid that a tribal boy would surpass his best student, Arjuna. He demanded that Ekalavya sacrifice his own right thumb as payment for learning under his name. Without questioning Drona, Ekalavya immediately cut off his right thumb and gave it to him, and was, therefore, unable to become the best archer in the world

Moral Lesson:
You will learn about hard work, respect and dedication, especially for teachers and instructors.'''

s2 = '''The Devotion of Surdas
Surdas was one of the greatest devotees of Lord Krishna. He loved Krishna so much that he wrote over a lakh of devotional songs in his honour. Surdas was a blind man, according to the story, who once took away Radha’s anklet when she was following him. When asked to return it, he refused, stating that he could not confirm her identity as he was blind. At this point, Krishna blessed him with sight, after which Surdas begged Krishna to take his sight away again. When asked why, he said that he had seen Krishna, and there was nothing else he wanted to see again.

Moral Lesson:
This story will teach you to love unconditionally and exhibit devotion towards the things he/she cares about.'''

s3 = '''The Courage of Abhimanyu
Abhimanyu was one of the greatest warriors in the Kurukshetra war. While his mother, Subhadra, was pregnant with him, his father, Arjuna, narrated the Chakravyuha battle formation technique to her. Abhimanyu learnt the entire technique, from the womb, but fell asleep right before Arjuna revealed how to escape the formation. During the war, Abhimanyu was trapped inside the Chakravyuha created by the Kaurava army. Even though he didn’t learn how to escape, he gave up his life fighting for his parents and family.

Moral Lesson:
Abhimanyu’s sacrifice will teach you about loyalty to family, bravery, dignity, and love.'''

s4 = '''The Integrity of Rama
Everyone knows of the Ramayana, the epic which chronicles the stories of the sixth incarnation of Mahavishnu, Lord Rama. In the Ramayana, Rama is forced to leave his kingdom and go into exile with his brother, Lakshmana, and wife, Sita. Near the end of his exile, Ravana, the king of Lanka, kidnaps his wife and holds her hostage. Facing all terrible odds, Rama manages to fight Ravana and his enormous army, and defeat them, rescuing his wife.

Moral Lesson:
The moral of this story is the bond shared between two brothers, and a husband and wife. It will teach you about friendship, integrity, and love.'''

s5= '''The Strength of Durga
When the asura-king Mahishasura defeats Indra, the king of the gods, and takes his place in heaven, the great goddess Durga is created from the divine energies of all the gods combined. She then takes on Mahishasura, the Buffalo Demon, and defeats him and his entire army, saving the world.

Moral Lesson:
Durga shows boys and girls that women, too, possess great courage, strength and righteousness.'''

s6 = '''The Faith of Prahlada
Prahlada, the son of the demon Hiranyakashipu, was a great Vishnu devotee. However, his arrogant father hated Vishnu, as he considered himself to be the one true God, due to the boon he had received from Lord Brahma. He tried to have Prahlada killed by many methods, but Prahlada was always saved by Vishnu. After Hiranyakashipu’s last attempt on Prahlada’s life, he got killed by Narasimha, the man-lion incarnation of Vishnu.

Moral Lesson:
This story will teach about the values of faith, devotion and patience.'''

s7 = '''The Focus of Arjuna
When the Pandavas were young, they trained under Drona, the master of combat. Drona wanted to test his pupils, so he stuck a toy bird in a tree and asked all of them to aim their bows at its eye. When he asked them what they could see, the Pandavas gave different answers, such as the bird, the leaves, the tree, and so on, and missed. Only Arjuna, without missing a beat, said he could see nothing more than the eye of the bird. Pleased, Drona asked Arjuna to shoot. Arjuna’s arrow pierced the bird’s eye, perfectly.

Moral Lesson:
This is a story about focus and determination, which will show you that knowing exactly what they want and working towards it will help them achieve their goals.'''

s8 = '''The Strength of Sita
After Rama and Sita returned to Ayodhya, they were crowned king and queen, and began a prosperous rule. However, rumours began to spread about Sita, who had lived with another man, Ravana (even though it was against her will). To control these rumours and ensure the continued faith of his subjects, Rama banished Sita to the forest, where she stayed with Valmiki. Here, she gave birth to twin boys and raised them as a single mother, all by herself.

Moral Lesson:
This story explains how, even in the face of such adversity, women can still be strong, brave, and independent.'''

s9 = '''The Loyalty of Shravana
Shravana was a poor teenage boy. helping his parents on a pilgrimage to all the religious sites in India. As they were old and blind, he was carrying them in two baskets slung over his shoulders. While crossing the forests of Ayodhya, Shravana is hit by a wayward arrow shot by Prince Dasharatha, and dies. Even with his dying breath, he begs Dasharatha to carry water to his thirsty parents.

Moral Lesson:
Shravana is the embodiment of kindness and loyalty. This story will help you understand the virtues of compassion and taking care of one’s parents.'''

s10 = '''The Patience of Mandodari
Mandodari was the wife of Ravana. While he performed misdeeds and cruelties, she spent her days trying her best to convince him to be just and honourable. She even asked him to free Sita, although her advice fell on deaf ears. Till the end, she stayed loyal to her husband.

Moral Lesson:
This lesson teaches you to be patient with loved ones, even if they are committing mistakes, without giving up on them. Loving someone means supporting them, even if not supporting their actions.'''

x = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
def hstory():
        l = choice(x)
        trans = Translator()
        tr = trans.translate(l.replace('"','').lower(),src='en',dest='hi')
        print(f"{Fore.YELLOW}Inspirational story: ",l)
        speak(tr.text, "hindiInspStory.mp3", "hi")
def story():
        l = choice(x)
        print(f"{Fore.YELLOW}Inspirational story: ",l)
        speak(l.replace('"', '').lower(), "InspStory.mp3")
if __name__ == "__main__":
        hstory()
        # story()
