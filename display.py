import requests
from datetime import datetime, timedelta

# ThingSpeak Configuration
CHANNEL_ID = "2894200"
READ_API_KEY = "MKATAB2OKYRZDE5Q"

def get_latest_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"
    response = requests.get(url)
    data = response.json()
    
    if not data.get('feeds'):
        print("No data available!")
        return
    
    latest = data['feeds'][0]
    
    print("\n=== Latest Sensor Data ===")
    print(f"Station ID : {latest.get('field4', 'N/A')}")
    print(f"Temperature: {latest['field1']} °C")
    print(f"Humidity   : {latest['field2']} %")
    print(f"CO₂        : {latest['field3']} ppm")
    print(f"Timestamp  : {latest['created_at']}")

def display_last_5_hours():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=5)
    
    url = (
        f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
        f"?api_key={READ_API_KEY}&start={start_time.isoformat()}&end={end_time.isoformat()}"
    )
    
    response = requests.get(url)
    data = response.json()
    
    feeds = data.get('feeds', [])
    if not feeds:
        print("\nNo data available for the last 5 hours.")
        return

    print("\n=== Last 5 Hours Sensor Data ===")
    print(f"{'Time':<25} {'Temp (°C)':<12} {'Humidity (%)':<15} {'CO2 (ppm)':<10}")
    print("-" * 65)
    
    for entry in feeds:
        time = entry['created_at']
        temp = entry.get('field1', 'N/A')
        hum = entry.get('field2', 'N/A')
        co2 = entry.get('field3', 'N/A')
        print(f"{time:<25} {temp:<12} {hum:<15} {co2:<10}")

if __name__ == "__main__":
    get_latest_data()
    display_last_5_hours()
