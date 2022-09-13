import requests
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your  api_key"
account_sid = "account_sid"
auth_token = "auth_token"

weather_params = {
    "lat": 31.01, ## lattitude 
    "lon": 8.65,  ## longtitude
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"]

will_rain = False
for h_w in hourly_weather[:12]:
    condition_code = h_w["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️☂️️",
        from_='+fromnumber',
        to='+tonumber'
    )

    print(message.status)
