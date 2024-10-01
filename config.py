USE_ROUNDED_COORDS = False
OPENWEATHER_API = 'c0ded68b5b342dd978ed322db542db9b'

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)