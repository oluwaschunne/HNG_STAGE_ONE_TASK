from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get("visitor_name", "Guest").strip('"')
    client_ip = request.remote_addr
    api_key = "9ebe49d50b414663bfd91107240107"

    if client_ip == "127.0.0.1":
        client_ip = "8.8.8.8"

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
