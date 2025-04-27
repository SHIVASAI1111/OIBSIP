import requests

def get_weather(city, api_key):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Change to 'imperial' for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f"\n🌍 Weather in {city.title()}:")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥️ Condition: {weather_description.capitalize()}")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError:
        print("⚠️ Error: City not found. Please check the name and try again.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def main():
    print("☀️ Welcome to the CLI Weather App!\n")
    api_key = input("🔑 Enter your OpenWeatherMap API Key: ").strip()
    city = input("🏙️ Enter the city name: ").strip()
    get_weather(city, api_key)

if __name__ == "__main__":
    main()

