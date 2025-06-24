import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------- CONFIGURATION --------
API_KEY = '1ac7c7a96eca31eccd4c409dea80ddd8'  # Replace with your actual OpenWeatherMap API key
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata']
weather_data = []

# -------- FETCH WEATHER DATA --------
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["main"]
        }
        weather_data.append(weather)
    else:
        print(f"Failed to get data for {city}")
        print(response.text)

# -------- CONVERT TO DATAFRAME --------
df = pd.DataFrame(weather_data)
print("\nWeather Data:\n", df)

# -------- MATPLOTLIB VISUALIZATION --------
plt.figure(figsize=(10, 5))
plt.bar(df['City'], df['Temperature (°C)'], color='skyblue')
plt.title('Temperature in Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------- SEABORN VISUALIZATION --------
plt.figure(figsize=(10, 5))
sns.barplot(x='City', y='Humidity (%)', data=df, palette='Blues_d')
plt.title('Humidity in Cities')
plt.ylabel('Humidity (%)')
plt.xlabel('City')
plt.grid(True)
plt.tight_layout()
plt.show()
