import requests
import config
def weather(city_name):
    complete_url=config.base_url+"?q="+city_name+"&appid="+config.api_key+"&units=metric"
    response=requests.get(complete_url)
    x=response.json()
    return x


