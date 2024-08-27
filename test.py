json = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1724403600, 'main': {'temp': 20.44, 'feels_like': 20.42, 'temp_min': 20.44, 'temp_max': 21.26, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 1002, 'humidity': 72, 'temp_kf': -0.82}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 83}, 'wind': {'speed': 9.16, 'deg': 214, 'gust': 18.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-08-23 09:00:00'}, {'dt': 1724414400, 'main': {'temp': 19.07, 'feels_like': 19.2, 'temp_min': 18.59, 'temp_max': 19.07, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 1005, 'humidity': 83, 'temp_kf': 0.48}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 9.04, 'deg': 244, 'gust': 16.07}, 'visibility': 10000, 'pop': 0.82, 'rain': {'3h': 0.82}, 'sys': {'pod': 'd'}, 'dt_txt': '2024-08-23 12:00:00'}, {'dt': 1724425200, 'main': {'temp': 21.43, 'feels_like': 20.93, 'temp_min': 21.43, 'temp_max': 21.43, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1008, 'humidity': 50, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 88}, 'wind': {'speed': 6.57, 'deg': 251, 'gust': 11.08}, 'visibility': 10000, 'pop': 0.2, 'rain': {'3h': 0.13}, 'sys': {'pod': 'd'}, 'dt_txt': '2024-08-23 15:00:00'}, {'dt': 1724436000, 'main': {'temp': 18.87, 'feels_like': 18.46, 'temp_min': 18.87, 'temp_max': 18.87, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1008, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 88}, 'wind': {'speed': 3.45, 'deg': 226, 'gust': 7.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-08-23 18:00:00'}], 'city': {'id': 2759794, 'name': 'Amsterdam', 'coord': {'lat': 52.3718, 'lon': 4.896}, 'country': 'NL', 'population': 2122311, 'timezone': 7200, 'sunrise': 1724387839, 'sunset': 1724438942}}


description_list = []
first = True
forecast = ""

for item in json["list"]:
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
        print(description_list)
        forecast += f" and {description}"

    print(group)
    print(description)

print(forecast)





