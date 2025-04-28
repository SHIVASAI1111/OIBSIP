import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    api_key = api_key_entry.get()
    if not api_key:
        messagebox.showerror("Error", "Please enter your API key!")
        return

    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_info.set(f"🌡️ Temp: {temp}°C\n🌥️ {condition.capitalize()}\n💧 Humidity: {humidity}%\n💨 Wind: {wind_speed} m/s")

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="City Name:").pack()
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Label(root, text="API Key:").pack()
api_key_entry = tk.Entry(root, width=30)
api_key_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_info = tk.StringVar()
tk.Label(root, textvariable=weather_info, font=("Helvetica", 12), justify="left").pack(pady=10)

root.mainloop()
