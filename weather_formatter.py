from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (
        f"{weather.city}, "
        f"temperature {weather.temperature}°C, "
        f"{weather.weather_type.value}\n"
        f"sunrise: {weather.sunrise.strftime('%H:%M')}\n"
        f"sunset: {weather.sunset.strftime('%H:%M')}\n"
    )

if __name__ == "__main__":                          #  test
    from datetime import datetime
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2024-09-26 07:00:00"),
        sunset=datetime.fromisoformat("2024-09-26 20:00:00"),
        city="Saint-Petersburg"
    )))