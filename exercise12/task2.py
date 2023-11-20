import requests

key = ""
cityname = input("Please enter the municipality")
geo_request = f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit=1&appid={key}"
geo_response = requests.get(geo_request).json()
weather_request = f"https://api.openweathermap.org/data/3.0/onecall?lat={geo_response[0]['lat']}&lon={geo_response[0]['lon']}&exclude=minutely,hourly,daily,alerts&appid={key}"
weather_response = requests.get(weather_request).json()
temperature = weather_response['current']['temp']-273.15
weather = weather_response['current']['weather'][0]['description']
print(f"Current weather in {cityname}: {weather}, {temperature:.0f} celsius.")
