import requests




key='3df4137afb5038ed8b916a7cff9e76bd'
api_address='https://api.openweathermap.org/data/2.5/weather?q=ciudad&lang=es&units=metric&appid='+key
json_data=requests.get(api_address).json()

def temp(ciudad= "Madrid"):
    x = api_address.replace('ciudad',ciudad)
    print(x)
    json_data=requests.get(x).json()
    temperature = str(round(json_data["main"]["temp"]))
    desc=json_data["weather"][0]["description"]
    return temperature,desc

print(temp()) 
print(temp("paris"))
