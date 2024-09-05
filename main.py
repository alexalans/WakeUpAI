import requests
from dotenv import load_dotenv
import os
import datetime as dt
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

data_collector = DataCollector(LATITUDE, LONGITUDE, WEATHER_API, NEWS_API)

prompt = (f"Write a wake up song for someone named {NAME}. Today is {dt.datetime.now().strftime('%A')}."
          f"Start with one verse about the weather today. It will rain {data_collector.weather['rain_mm']} millimeter."
          f"The temperature is going to be {data_collector.weather['temperature']} degrees "
          f"(it feels like {data_collector.weather['feel_temperature']})."
          f"The weather can be described as {''.join(data_collector.weather['description'])}."
          f"The second verse includes a reminder about the person's to do list."
          f"Alexa wants to do yoga today, work on her coding skills and go for a run."
          f"Also she has to get motivated to play some guitar."
          f"For the bridge of the song, use information about the latest news. "
          f"You can use this input for that: "
          f"Please keep the news short and summarised."
          f"{data_collector.news}"
          f"Now comes a verse with a random useless fact: "
          f"Did you know that {data_collector.random_fact}?"
          f"The last verse will contain some inspiration life advice to start the day."
          f"Please come up with an inspirational motivational quote to get {NAME} out of bed.")

print(prompt)

test_genre = "ROCK ELECTRO SWING BOOGIE"
test_title = "TEST TITLE"

for i in range(5):
    try:
        pyautogui.scroll(200)
        time.sleep(0.1)
        pyautogui.click('pyautogui_images/message_chatgpt.png')
        time.sleep(2)
        pyautogui.write(f"{prompt}")
        time.sleep(5)
    except ImageNotFoundException:
        pyautogui.keyDown('alt')
        for _ in range(i):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        time.sleep(0.1)
    else:
        pyautogui.press('enter')
        time.sleep(30)
        pyautogui.click(x=500, y=500)
        break

pyautogui.hotkey('ctrl', 'shift', 'c')
time.sleep(1)
pyautogui.hotkey('ctrl', 'tab')

time.sleep(1)
pyautogui.click('pyautogui_images/enter_lyrics2.png')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'a', 'delete')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click('pyautogui_images/enter_style.png')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'a', 'delete')
time.sleep(0.1)
pyautogui.write(f"{test_genre}")

pyautogui.scroll(-500)
time.sleep(0.1)

pyautogui.click('pyautogui_images/enter_title.png')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'a', 'delete')
time.sleep(0.1)
pyautogui.write(f"{test_title}")

pyautogui.scroll(-1000)
time.sleep(1)
pyautogui.click('pyautogui_images/create.png')


#TODO SAVE LYRICS IN FILE




