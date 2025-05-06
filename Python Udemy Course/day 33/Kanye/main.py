import requests
import datetime as dt

MY_LAT = 44.623219
MY_LNG = 21.187189

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "format": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("AM")[1].split(":")[0]
sunset = data["results"]["sunset"]
print(sunrise)

time_now = dt.datetime.now()
