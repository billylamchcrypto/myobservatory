from dataclasses import dataclass

import requests


class Utils:
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"

    def connect_api(self, data_type, lang):
        headers = {'content-type': 'application/json'}
        params = {'dataType': data_type, 'lang': lang}
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def get_status(self, data_type, lang):
        response = self.connect_api(data_type, lang)
        assert response.status_code == 200
        pass

    def get_data(self, data_type, lang):
        response = self.connect_api(data_type, lang)
        data = response.json()

    def humidity_of_day_after_tmr(self):
        pass



# @dataclass
# class WeatherInfo:
#     temp: float
#     sunset: str
#     sunrise: str
#     temp_min: float
#     temp_max: float
#     desc: str
#
#     @classmethod
#     def from_dict(cls, data: dict) -> 'WeatherInfo':
#         return cls(
#             temp=data["main"]["temp"],
#             temp_min=data["main"]["temp_min"],
#             temp_max=data["main"]["temp_max"],
#             desc=data["weather"][0]["main"],
#             sunset=format_date(data["sys"]["sunset"]),
#             sunrise=format_date(data["sys"]["sunrise"]),
#             )