# Companion
Welcome to your real Companion! This assistant provides a wide range of features and functionalities to assist you with various tasks. Before using all the features, please follow the setup instructions below.
This repository can become your real companion. Python scripts in this repository use some amazing applications of python language. This assistant provides a wide range of features and functionalities to assist you with various tasks.

![Companion-3-Screenshot 2023-07-16 131001](https://github.com/SinghIsWriting/companion/assets/122283853/7ecc6e4b-2c6a-48b7-969e-cd53abb1edf0)


## Getting Started
To get started, follow the instructions below to clone the repository and run the main script.

## Prerequisites
* Python 3.x
* Git (optional)

## Installation
1. Clone the repository to your local machine using the following command:
```
git clone https://github.com/SinghIsWriting/companion.git
```
2. Alternatively, you can download the repository as a ZIP file and extract it.
3.  Navigate to the project directory:
```python
cd companion
```
4. Install any required dependencies:
```python
pip3 install -r requirements.txt
```
5. Now proceed to setup.

## Setup
To set up the assistant and use all the features, please perform the following actions:

1. Set a password in the specified file `txt/passwd.txt` to ensure secure access.
2. Set a owner's name in the specified file `txt/owner.txt`  or you can command during the conversation to the program to change/reset the owner's name.
3. Add your and your relatives birth dates to the `csv/bdays.csv` file for the assistant to provide birthday reminders.
4. Obtain an API key from `OpenWeatherMap` and add it to the appropriate location in the code to enable weather information retrieval. To do the same, visit https://api.openweathermap.org/ and Signin/Signup then generate your own API Key.
5. Obtain an app ID from `WolframAlpha` and add it to the code to enable mathematics and scientific queries. To do the same, visit https://www.wolframalpha.com/ and Signin/Signup then generate your own APP ID.
6. Add your favorite songs to the `mp3/songs/` folder for the assistant to play on request with song name, and you can play more songs on Spotify.
7. Configure the News API in the `news.py` file to retrieve recent news updates. To do the same, visit https://newsapi.org/ and Signin/Signup then generate your own API Key.
8. Obtain a NASA API key and add it to the `nasa.py` file for accessing NASA updates and asteroid tracking. To do the same, visit https://api.nasa.gov/ and Signin/Signup then generate your own API Key.

## Usage
1. Run the main.py script:
```python
python3 main.py
```
2. Now after entering your password you can start a conversation with your true companion
3.  Take a look on some major features of this companion program.

## Features
The Companion program offers the following major features:

1. Show System ID: Display system identification information. Just say ```show system id```
2. Chat: Engage in a conversation and ask common questions as date, time, who is it, greetings, age, etc. Just say ```what is/tell me date```
3. Weather Information: Retrieve weather information for any city using OpenWeatherMap. Just say ```weather of/in CITY```
4. Mathematics and Scientific Queries: Perform calculations and obtain scientific answers using WolframAlpha. Just say ```solve question or I have a query```
5. Wikipedia Information: Access information from Wikipedia. Just say ```tell me about DEMOCRACY```
6. Calendar: Display the calendar for any year and month. Just say ```calendar of JULY 2023```
7. Play Music: Play songs on Spotify. Just say ```play/sing SONG_NAME```
8. COVID Info: Obtain COVID-19 information. Just say ```give me COVID information```
9. Recent News Updates: Get the latest news updates. Just say ```Sports news```
10. Translation: Translate text between Hindi and English or any language to English. Just say ```translate TEXT/ translate TEXT in english```
11. Open System Apps: Launch specified system applications. Just say ```open powershell/instagram/notepad/file explorar/command prompt/youtube/facebook/...```
12. Google Search: Search for any information on Google. Just say ```search YOUR_TOPIC```
13. IP Scanning: Retrieve your IP address and scan specific ports. Just say ```scan my IP```
14. NASA Updates: Get updates from NASA. Just say ```NASA updates today```
15. Asteroid Tracking: Track asteroids. Just say ```track asteroids today```
16. Open Map: Open a map in a web browser. Just say ```show map of CITY```
17. Upcoming Movies: Get a list of new upcoming movies. Just say ```show me upcoming/movies list/table``` 
18. Movie Search: Search for information about any movie. Just say ```MOVIE_NAME movie```
19. Entertaining content: Get funny Text, Jokes, and Interesting Facts. Just say ```tell me a joke/funny/fact```
20. Currency Conversion: Retrieve the values of various currencies. Just say ```currency_name```
21. Motivational Quotes, Mythological and Inspirational Stories: Access stories and quotes in Hindi and English. Just say ```tell me a inspirational/mythological story [hindi] or motivational quote```
22. Diet/Food Nutrition: Obtain nutritional information for various foods and beverages. Just say ```nutrition of VEGETABLES/FRUITE/NUTS/OILS/DESSERTS... or nutrition table/list```
23. MNC's Table: Retrieve a table/list of MNC's founders, CEOs, revenue, and headquarters. Just say ```table/list of FOUNDERS/REVENUE/CHIEF/CEOS/HEADQUARTERS of companies```
24. Government Information: Get a table/list of PMs, Presidents, CMs, population of a country/state, and crimes in a city in India. Just say ```PM/President/CM/Population of COUNTRY or crimes in city_name```
25. Newly Launched Mobiles and Govt Jobs: Stay updated on new mobile phone launches and government job vacancies. Just say ```list/table of latest mobiles/government jobs```
26. Note making: Write and save notes. Just say ```make/write a note YOUR TEXT```
27. Package Version: Get the version of any installed package. Just say ```show release details```

## Contributing
Contributions to this repository are welcome. If you would like to add additional features or improve existing ones, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test your changes thoroughly.
5. Commit your changes with a descriptive commit message.
6. Push your changes to your forked repository.
7. Create a pull request detailing your changes.
