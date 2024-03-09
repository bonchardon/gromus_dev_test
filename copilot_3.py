import requests
import json


# Function to interact with Copilot API
def interact_with_copilot(endpoint, question):
    # Define API endpoints
    ENDPOINTS = {
        'Influencer': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/Influencer',
        'InfluencerData': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/InfluencerData',
        'Music': 'https://flaidata.tiktok-alltrends.com:442/api/datapoint/Music'
    }

    # Make GET request to Copilot
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJEYXRhUG9pbnRTZWNyZXQiOiI0NWUxY2UyNy05Y2UzLTQ0ZjQtYTAzNC0wM2MzZGE1M2VlZTMiLCJuYmYiOjE3MDk4MTA3ODEsImV4cCI6MTcxMjQ4OTE4MSwiaWF0IjoxNzA5ODEwNzgxLCJpc3MiOiJTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ.q61C-P46IoZYKD9xhj8g6M4GgPU_IsggJNd0jeBhjXc'
    headers = {'Token': token}
    params = {'question': question}
    response = requests.get(ENDPOINTS[endpoint], headers=headers, params=params)

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


print(interact_with_copilot('Influencer', "Hi GE: Could you analyze my account?https://www.tiktok.com/@im_mmxvii"))
