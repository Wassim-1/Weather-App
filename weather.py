import requests
import config
def weather(city_name):
    complete_url=config.base_url+"?q="+city_name+"&appid="+config.api_key+"&units=metric"
    response=requests.get(complete_url)
    x=response.json()
    # temp=str(x["main"]["temp"])+"°C"
    # feels=str(x["main"]["feels_like"])+"°C"
    # humidity=str(x["main"]["humidity"])+"%"
    # weather=x["weather"][0]["main"]
    # details=x["weather"][0]["description"]
    # print("weather:" ,weather)
    # print("details: ",details)
    # print("temp= ",temp)
    # print("feels like: ",feels)
    # print("humidity= ",humidity)
    # print(x)
    return x


