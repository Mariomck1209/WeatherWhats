# Project: Weather Update via WhatsApp

This project uses the Twilio API to send information about the current weather of a specific location via a WhatsApp message. The weather data is obtained from the OpenWeatherMap API.

## Project Files

### 1. **main.py**
This file contains the main code that interacts with the Twilio API and the OpenWeatherMap API.

#### Functionality:
- It fetches weather information for a location using the `get_weather` function from **weatherapp.py**.
- It displays the weather data using the `show_weather` function from **weatherapp.py**.
- It uses the Twilio API to send a WhatsApp message with the weather data to the specified number.

#### Requirements:
- **Twilio Account SID and Auth Token**: Required for authenticating the connection with the Twilio API.
- **OpenWeatherMap API Key**: You need an API key to access the weather data from OpenWeatherMap.

#### Workflow:
1. It retrieves the latitude and longitude of the location.
2. It makes a request to the OpenWeatherMap API to get the weather data.
3. It displays the weather in a readable format.
4. It sends a WhatsApp message with the weather information.

### 2. **weatherapp.py**
This file contains functions that interact with the OpenWeatherMap API to get and display weather information.

#### Functionality:
- **get_weather**: Makes an HTTP GET request to the OpenWeatherMap API with the latitude, longitude, and API key provided. If the request is successful, it returns the weather data in JSON format.
- **show_weather**: Takes the weather data in JSON format and returns a string with detailed weather information, such as temperature, humidity, atmospheric pressure, wind speed, and more.

### How to Run the Project:

1. Install the required dependencies:
   - Make sure to install the necessary libraries:
     ```bash
     pip install requests twilio
     ```

2. Get your credentials:
   - Sign up at [Twilio](https://www.twilio.com/) to get your Account SID and Auth Token.
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API Key.

3. Set up the credentials in **main.py**:
   - Replace the `account_sid`, `auth_token`, and `apiKey` variables with your own credentials.

4. Run the `main.py` script:
   ```bash
   python main.py

