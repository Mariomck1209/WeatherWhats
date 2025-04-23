import schedule
import time
from twilio.rest import Client
import weatherapp
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def send_messages():
    lat: float = 10.3052405
    lon: float = -84.8209913
    apiKey: str = os.getenv("OPENWEATHER_API_KEY")

    clima_hoy = weatherapp.get_weather(lat, lon, apiKey)
    mostrar_clima = weatherapp.show_weather(clima_hoy)

    # Cargar credenciales de Twilio desde variables de entorno
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    # Crear cliente de Twilio
    client = Client(account_sid, auth_token)

    # Enviar mensaje por WhatsApp
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Número de sandbox de Twilio
        body=mostrar_clima,
        to='whatsapp:+50686809821'  # Tu número de WhatsApp con código de país
    )

    print(f"Mensaje enviado. SID: {message.sid}")

# Programar el envío del mensaje todos los días a las 9:00 AM
schedule.every().day.at("9:00").do(send_messages)

# Ejecutar el código de manera continua para que se ejecute a la hora programada
while True:
    schedule.run_pending()
    time.sleep(60)
