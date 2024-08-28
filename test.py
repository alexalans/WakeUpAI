import requests

fact_response = requests.get(url="https://uselessfacts.jsph.pl/api/v2/facts/today")

fact = fact_response.json()['text']