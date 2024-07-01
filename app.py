from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def fetch_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    data = response.json()
    return data["ip"]


@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get("visitor_name", "Guest").strip('"')

    if request.headers.get("X-Forwarded-For"):
        client_ip = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    else:
        client_ip = request.remote_addr

    # If running locally, use the public IP for demonstration purposes
    if client_ip == "127.0.0.1":
        client_ip = fetch_public_ip()

    api_key = os.getenv('WEATHER_API_KEY')

    # Get weather and location information
    weather_response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={client_ip}')
    weather_data = weather_response.json()

    if 'location' in weather_data and 'current' in weather_data:
        city = weather_data['location']['name']
        temperature = weather_data['current']['temp_c']
    else:
        print(f"Error: Unable to get location and temperature for IP {client_ip}. API response:{weather_data}")
        city = "Unknown"
        temperature = "N/A"

    response_data = {
        'client_ip': client_ip,
        'location': city,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
