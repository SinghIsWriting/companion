from colorama import Fore, init
init(autoreset=True)
from imdb import IMDb
from datetime import datetime
from path import path
from speak import speak

def search_movie(text):
    print("Searching for... " + text.title())
    # gathering information from IMDb
    moviesdb = IMDb()
    # passing input for searching movie
    movies = moviesdb.search_movie(text)
    if len(movies) == 0:
        print(f"{Fore.YELLOW}\nNo result found")
    else:
        print(f"{Fore.GREEN}\nI found this:")
        title = ""
        year = ""
        plot = ""
        rating = ""
        for movie in movies:
            try:
                info = movie.getID()
                movie = moviesdb.get_movie(info)

                title = movie['title']
                year = movie['year']
                # speaking title with releasing year
                print(f'{title}-{year}')

                title = movie['title']
                year = movie['year']
                rating = movie['rating']
                plot = movie['plot outline']
                # the below if-else is for past and future release
                if year < int(datetime.now().strftime("%Y")):
                    re = f'''{Fore.YELLOW}{title} was released in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is {plot}'''
                    print(re)
                    speak(re, "moviesIMDB.mp3")
                    break
                else:
                    re = f'''{Fore.YELLOW}{title} will release in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is {plot}'''
                    print(re)
                    speak(re, "moviesIMDB.mp3")
                    break
            except:
                print(f"{Fore.RED}Opps, something went wrong!")
    print()
if __name__ == "__main__":
    mov = input("Enter the movie name here: ")
    search_movie(mov)
