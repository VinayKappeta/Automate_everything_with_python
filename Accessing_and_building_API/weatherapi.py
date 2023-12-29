#https://api.openweathermap.org/data/2.5/forecast?q=Aleppo&APPID=26631f0f41b95fb9f5ac0df9a8f43c92&units=metric

import requests

def get_weather(city = 'Aleppo',units = 'metrics',apiKey ='26631f0f41b95fb9f5ac0df9a8f43c92'):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units={units}")
    content = r.json()
    #print(articles['list'])
    print(content)
    with open('/config/workspace/Accessing_and_building_API/data.txt','a') as file:
        for i in (content['list']):
            file.write(f"{city},{i['dt_txt']},{i['main']['temp']},{i['weather'][0]['description']}\n")
            print(f"{city},{i['dt_txt']},{i['main']['temp']},{i['weather'][0]['description']}\n")

print(get_weather(city='Washington'))