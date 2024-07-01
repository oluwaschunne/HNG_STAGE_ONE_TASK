from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr
    api_key = '9ebe49d50b414663bfd91107240107'

    # Get weather and location information
    weather_response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={client_ip}')
    weather_data = weather_response.json()
    city = weather_data['location']['name']
    temperature = weather_data['current']['temp_c']

    response_data = {
        'client_ip': client_ip,
        'location': city,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
