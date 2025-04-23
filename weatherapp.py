import requests
from typing import Any



def get_weather(lat: float, lon: float, apiKey: str) -> dict | None:
    url: str = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&units=metric&lang=es"
    try:
        res = requests.get(url)
        res.raise_for_status()  # Lanza una excepción si el status no es 200
        return res.json()
    except requests.RequestException as e:
        print(f"❌ Error al obtener el clima: {e}")
    return None
    

def show_weather(data: dict[str, Any] | None) -> str:
    if not data:
        return

    main = data.get("main", {})
    weather: dict[str, Any] = data.get("weather", [{}])[0]
    wind = data.get("wind", {})
    
    return (
        f"📍 Ciudad: {data.get('name', 'Desconocida')} "
        f"📝 Descripción: {weather.get('description', 'N/A')}"
        f"🌡️ Temperatura: {main.get('temp', 'N/A')}°C"
        f"🌡️ Sensación térmica: {main.get('feels_like', 'N/A')}°C"
        f"🌡️ Temp. máxima: {main.get('temp_max', 'N/A')}°C"
        f"🌡️ Temp. mínima: {main.get('temp_min', 'N/A')}°C"
        f"💧 Humedad: {main.get('humidity', 'N/A')}%"
        f"🌀 Presión atmosférica: {main.get('pressure', 'N/A')} hPa"
        f"🌬️ Vel. del viento: {wind.get('speed', 'N/A')} m/s"
        f"***********ENGLISH VERSION**********"
        f"📍 City: {data.get('name', 'Desconocida')} "
        f"📝 Description: {weather.get('description', 'N/A')}"
        f"🌡️ Temperature: {main.get('temp', 'N/A')}°C"
        f"🌡️ Feels like: {main.get('feels_like', 'N/A')}°C"
        f"🌡️ Max temp: {main.get('temp_max', 'N/A')}°C"
        f"🌡️ Min temp: {main.get('temp_min', 'N/A')}°C"
        f"💧 Humidity: {main.get('humidity', 'N/A')}%"
        f"🌀 Atmospheric pressure: {main.get('pressure', 'N/A')} hPa"
        f"🌬️ Wind speed: {wind.get('speed', 'N/A')} m/s"
    )



