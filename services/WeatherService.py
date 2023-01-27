import requests

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url_base = "https://openweathermap.org/data/2.5"

    def get_location_id(self, city):
        city = self.__create_location_string(city)
        url = f"{self.url_base}/find?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            id = response.json().get("list")[0].get("id")
            return id
        except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
            print(e)
            return e

    def get_weather_by_id(self, id):
        url = f"{self.url_base}/weather?id={id}&appid={self.api_key}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                current_temp = self.__convert_c_to_f(
                    response.json().get("main").get("temp"))
                description = response.json().get(
                    "weather")[0].get("description")
                return (f"```Temperature: {int(current_temp)}F\nDescription: {description}```")
        except (requests.ConnectionError, requests.HTTPError, requests.Timeout) as e:
            print(e)
            return e

    def __create_location_string(self, city):
        if len(city) > 1:
            city = city.split(' ')
            return "%20".join(city)
        else:
            return city

    def __convert_c_to_f(self, temp):
        return temp * 9/5 + 32