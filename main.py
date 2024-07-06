import requests

# https://home.openweathermap.org/
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your api key password"
# https://api.openweathermap.org/data/2.5/weather?q=Lahore,pk%20&appid=07155a9d8c4a8c99c69394560c88f536
weather_params = {
    "lat": 31.561920,
    "lon": 74.348083,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
# print(response.json())
will_rain = False
for hour_data in weather_data["list"]:
    # print(hour_data["weather"])
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Umbrella")
