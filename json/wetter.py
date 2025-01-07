import requests

response = requests.get("https://wttr.in/berlin?format=j1")
daten = response.json()
# jetzt sind die json daten in der variable daten gespeichert
# print(daten)
# print(daten["current_condition"][0]["temp_C"])
temperatur = daten["current_condition"][0]["temp_C"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
print(wetter)
print(f"The weather in Berlin is {wetter} with {temperatur}°C")