import requests
import json

# Replace with your actual API key
API_KEY = '_API_KEY_'

# Define the API endpoint
url = f"https://speech.googleapis.com/v1/speech:recognize?key={API_KEY}"

# Construct the request payload
payload = {
    "config": {
        "encoding": "FLAC",
        "languageCode": "en-US"
    },
    "audio": {
        "uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
    }
}

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Write the JSON response to a file
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

print("Speech recognition result saved to 'result.json'")
