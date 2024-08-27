class WeatherBard:
    def __init__(self, weather_data):
        self.rain_mm = 0
        self.data = weather_data
        self.lyrics = self.temperature() + self.forecast() + self.rain_count()

    def rain_count(self):
        for item in self.data["list"]:
            try:
                self.rain_mm += item['rain']['3h']
            except KeyError:
                pass
        if self.rain_mm > 50:
            return ". \nHoly shit, \nthere's a lotta rain forecasted. \nI hope you've got an inflatable canoe"
        elif self.rain_mm > 30:
            return ". \nBetter stay inside, \nit's going to be raining violently today. \nGoooood luck!"
        elif self.rain_mm > 20:
            return ". \nUh-oh, it'll be raining heavily today.\n Maybe bring an umbrella."
        elif self.rain_mm > 10:
            return ". \nLooks like it's gonna be a rainy day!"
        elif self.rain_mm > 2:
            return ". \nThere's really not that much rain today"
        elif self.rain_mm > 0.2:
            return ". \nExpect just a little bit of drizzle, maybe"
        else:
            return "No rain today, hurray!"

    def forecast(self):
        description_list = []
        forecast = ""
        first = True
        for item in self.data["list"]:
            group = int(str(item["weather"][0]["id"])[0])
            description = item["weather"][0]["description"]
            if group == "2":
                description = f"a {description}"
            if first:
                description_list.append(group)
                forecast += f"Expect {description}"
                first = False
                continue
            if group not in description_list:
                description_list.append(group)
                forecast += f" and {description}"
        return forecast

    def temperature(self):
        temp = round(self.data["list"][1]["main"]["temp"])
        feels_like = round(self.data["list"][1]["main"]["temp"])
        if temp == feels_like:
            return f"Today It'll be {temp} degrees \nand that is what it feels like\n"
        else:
            return f"Today it's gonna be {temp} degrees \nbut it will feel like {feels_like}\n"


