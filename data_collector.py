import requests

class DataCollector:
    def __init__(self, latitude, longitude, weather_api, news_api):
        self.weather = {}
        self.get_weather_data(latitude, longitude, weather_api)
        self.news = ''
        self.get_news_data(news_api)
        self.random_fact = self.get_random_fact()

    def get_weather_data(self, latitude, longitude, weather_api):
        weather_parameters = {
            "lat": latitude,
            "lon": longitude,
            "units": "metric",
            "cnt": 5,
            "appid": weather_api,

        }

        weather_response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                                        params=weather_parameters)
        weather_response.raise_for_status()

        weather_data = weather_response.json()

        rain_mm = 0
        for item in weather_data["list"]:
            try:
                rain_mm += item['rain']['3h']
            except KeyError:
                pass

        self.weather['temperature'] = round(weather_data["list"][1]["main"]["temp"])
        self.weather['feel_temperature'] = round(weather_data["list"][1]["main"]["temp"])
        self.weather['description'] = [item["weather"][0]["description"] + ', ' for item in weather_data["list"]]
        self.weather['rain_mm'] = round(rain_mm)
        print(self.weather)

    def get_news_data(self, news_api):
        news_parameters = {
            "apikey": news_api,
            "category": "science, technology, environment, tourism",
            "language": "en",
            "prioritydomain": "top",
            "domainurl": "nytimes.com, bbc.com, aljazeera.com",
            "size": 3,
        }

        news_response = requests.get(url="https://newsdata.io/api/1/latest", params=news_parameters)

        news_response.raise_for_status()

        news_data = news_response.json()['results']

        for item in news_data:
            self.news += f"{item['title']}: {item['description']}."

    def get_random_fact(self):
        fact_response = requests.get(url="https://uselessfacts.jsph.pl/api/v2/facts/today")

        fact = fact_response.json()['text']
        print(fact)

        return fact


        news_response.raise_for_status()


#TODO GET TODO LIST FROM GOOGLE SHEETS OR TODOIST API


#TODO USE BEAUTIFUL SOUP TO OBTAIN HOROSCOPE TEXT OR ASK CHATGPT TO COME UP WITH NONSENSE

