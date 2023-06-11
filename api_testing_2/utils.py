import datetime
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
        return data

    @staticmethod
    def get_today():
        current_date = datetime.date.today()
        date_string = current_date.strftime("%Y%m%d")
        return date_string

    def humidity_of_day_after_tmr(self, data_type, lang):
        data = self.get_data(data_type, lang)
        forecast_date = Utils.get_today()
        forecast_date = int(forecast_date) + 2
        forecast_date = str(forecast_date)

        for forecast in data["weatherForecast"]:
            if forecast["forecastDate"] == forecast_date:
                forecast_min_rh = str(forecast["forecastMinrh"]["value"])
                forecast_max_rh = str(forecast["forecastMaxrh"]["value"])
                print("The humidity of the day after tomorrow is " + forecast_min_rh + "-" + forecast_max_rh + "%")
                break

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
