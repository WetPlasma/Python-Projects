import requests
import os


api_key = os.environ.get("weather_api_key")

api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 21.007658,
    "lon": 75.562607,
    "appid": api_key,
}
response = requests.get(api_endpoint, params=weather_params)
print(response.status_code)

weather_data = response.json()
if weather_data["weather"][0]["id"] < 700:
    print("Bring an umbrella")
else:
    print("Clear skies ahead")
