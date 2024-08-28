import requests
from dotenv import load_dotenv
import os
import datetime
import time
import pyautogui
import PIL
from data_collector import DataCollector
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

data_collector = DataCollector(LATITUDE, LONGITUDE, WEATHER_API, NEWS_API)

prompt = (f"Write a wake up song for someone named Alexa. \n"
          f"Start with one verse about the weather today. It will rain {data_collector.weather['rain_mm']} millimeter.\n"
          f"The temperature is going to be {data_collector.weather['temperature']} degrees and "
          f"it feels like {data_collector.weather['feel_temperature']}.\n"
          f"The weather can be described as {''.join(data_collector.weather['description'])}.\n\n"
          f"The second verse includes a reminder about the person's to do list.\n"
          f"Alexa wants to do yoga today, work on her coding skills and go for a run.\n"
          f"Also she has to get motivated to play some guitar.\n\n"
          f"For the bridge of the song, use information about the latest news. "
          f"You can use this input for that: \n"
          f"Please keep the news short and summarised."
          f"{data_collector.news}")

print(prompt)

#TODO SAVE LYRICS IN FILE



test_lyrics = "TEST LYRICS"
test_genre = "ROCK ELECTRO SWING BOOGIE"
test_title = "TEST TITLE"

# for i in range(5):
#     try:
#         pyautogui.scroll(200)
#         time.sleep(0.1)
#         pyautogui.click('pyautogui_images/enter_lyrics.png')
#         pyautogui.write(f"{test_lyrics}")
#         time.sleep(0.5)
#     except ImageNotFoundException:
#         pyautogui.keyDown('alt')
#         for _ in range(i):
#             pyautogui.press('tab')
#         pyautogui.keyUp('alt')
#         time.sleep(0.1)
#     else:
#         break
#
#
# pyautogui.click('pyautogui_images/enter_style.png')
# pyautogui.write(f"{test_genre}")
#
# pyautogui.scroll(-250)
# time.sleep(0.1)
#
# pyautogui.click('pyautogui_images/enter_title.png')
# pyautogui.write(f"{test_title}")
#
# pyautogui.click('pyautogui_images/create.png')







