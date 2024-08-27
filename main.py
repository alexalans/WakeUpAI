# ON HOLD | Suno does not have its own API and I cannot get the external APIs to work,
# also cannot open a new automated browser because Google refuses to login user when
# it knows you're botting. Possible solutions: open a different kind of browser,
# try different login process (no authentication with Google), wait for Suno to release its own API.

#For now.... just make it work on laptop with a trusted browser already opened and let pyautogui move around in it...

import requests
from dotenv import load_dotenv
import os
import datetime
from weather_bard import WeatherBard
from news_bard import NewsBard
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import PIL
from pyautogui import ImageNotFoundException

#TODO move all preferences / settings to the top or different doc

# GET ENVIRONMENT VARIABLES
load_dotenv()

NAME = os.environ['YOUR_NAME']
LATITUDE = os.environ['YOUR_LATITUDE']
LONGITUDE = os.environ['YOUR_LONGITUDE']

# OPEN_AI_API = os.environ['OPEN_AI_API']
WEATHER_API = os.environ['WEATHER_API']
NEWS_API = os.environ['NEWS_API']

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

#START LYRICS

lyrics = (f"Hey there {NAME},\n"
          f"a good morning to you,\n"
          f"wake up, wake up,\n"
          f"it's time to start the day\n\n")

# GET LOCAL WEATHER FROM OPEN WEATHER

# weather_parameters = {
#     "lat": LATITUDE,
#     "lon": LONGITUDE,
#     "units": "metric",
#     "cnt": 5,
#     "appid": WEATHER_API,
#
# }
#
# weather_response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
# weather_response.raise_for_status()
#
# weather_data = weather_response.json()
# lyrics += WeatherBard(weather_data).lyrics

#GET NEWS
#
# news_parameters = {
#     "apikey": NEWS_API,
#     "category": "science",
#     #"country": "uk",
#     "language": "en",
#     "prioritydomain": "top",
#     "domainurl": "nytimes.com, bbc.com, aljazeera.com",
#     "size": 3,
# }
#
# news_response = requests.get(url="https://newsdata.io/api/1/latest", params=news_parameters)
#
# news_response.raise_for_status()
#
# news_data = news_response.json()
#
# lyrics += NewsBard(news_data).lyrics

#TODO GET TODO LIST FROM GOOGLE SHEETS OR TODOIST API


#TODO USE BEAUTIFUL SOUP TO OBTAIN HOROSCOPE TEXT OR ASK CHATGPT TO COME UP WITH NONSENSE


#TODO ADD GOOGLE CALENDAR EVENTS


#TODO SAVE LYRICS IN FILE


#TODO CREATE LYRICS

#TODO CREATE SONG

test_lyrics = "TEST LYRICS"
test_genre = "ROCK ELECTRO SWING BOOGIE"
test_title = "TEST TITLE"

for i in range(5):
    try:
        pyautogui.scroll(200)
        time.sleep(0.1)
        pyautogui.click('pyautogui_images/enter_lyrics.png')
        pyautogui.write(f"{test_lyrics}")
        time.sleep(0.5)
    except ImageNotFoundException:
        pyautogui.keyDown('alt')
        for _ in range(i):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(0.1)
    else:
        break

pyautogui.click('pyautogui_images/enter_style.png')
pyautogui.write(f"{test_genre}")

pyautogui.scroll(-250)
time.sleep(0.1)

pyautogui.click('pyautogui_images/enter_title.png')
pyautogui.write(f"{test_title}")

pyautogui.click('pyautogui_images/create.png')







