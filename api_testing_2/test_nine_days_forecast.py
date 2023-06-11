from api_testing_2.utils import Utils

# data type params
LOCAL_WEATHER_FORECAST = "flw"
NINE_DAYS_WEATHER_FORCAST = "fnd"
CURRENT_WEATHER_REPORT = "rhrread"

# language params
TRAD_CHINESE = "tc"
SIMP_CHINESE = "sc"
ENGLISH = "en"


def test_one():
    run = Utils()
    a = "fnd"
    b = "en"
    run.get_status(a, b)
    run.get_data(a, b)
    run.humidity_of_day_after_tmr(a,b)
