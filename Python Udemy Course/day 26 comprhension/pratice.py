weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {}
for k,v in weather_c.items():
    v = (v * 9/5) + 32 
    weather_f.update({k:v})
print(weather_f)
