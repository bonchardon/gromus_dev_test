from flask import render_template, Flask, jsonify
import requests
import json
from template import *

app = Flask(__name__, template_folder='template')


# Define the interact_with_copilot function
def interact_with_copilot(endpoint):
    # Define API endpoints
    ENDPOINTS = {
        'Influencer': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/Influencer',
        'InfluencerData': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/InfluencerData',
        'Music': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/Music'
    }

    # Make GET request to Copilot
    token = str(
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJEYXRhUG9pbnRTZWNyZXQiOiI0NWUxY2UyNy05Y2UzLTQ0ZjQtYTAzNC0wM2MzZGE1M2VlZTMiLCJuYmYiOjE3MDk4MTA3ODEsImV4cCI6MTcxMjQ4OTE4MSwiaWF0IjoxNzA5ODEwNzgxLCJpc3MiOiJTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ.q61C-P46IoZYKD9xhj8g6M4GgPU_IsggJNd0jeBhjXc')
    headers = {'Token': f'{token}'}
    response = requests.get(ENDPOINTS[endpoint], headers=headers)

    # Check if the response is successful and contains content
    if response.status_code == 200 and response.content:
        try:
            return response.json()
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


@app.route('/get_copilot_data/<string:endpoint>')
@app.route('/')
def copilot_and_home(endpoint=None):
    if endpoint:
        # If an endpoint is provided, fetch data from Copilot
        data = interact_with_copilot(endpoint)
        if data:
            print(data)
            return jsonify(data)
        else:
            return jsonify({'error': 'Failed to fetch data from Copilot'}), 500
    else:
        # If no endpoint is provided, render the home template
        return render_template('h1.html')


if __name__ == '__main__':
    app.run(debug=True)
