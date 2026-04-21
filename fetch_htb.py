import os
import requests
import json

# Your HTB ID for the Labs platform
USER_ID = "1510537"
API_TOKEN = os.environ.get("HTB_API_TOKEN")

# HTB Labs API Endpoint
url = f"https://labs.hackthebox.com/api/v4/user/profile/activity/{USER_ID}"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Save the data to a local JSON file
        with open("htb_activity.json", "w") as f:
            json.dump(response.json(), f)
        print("Successfully fetched HTB activity.")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        
except Exception as e:
    print(f"An error occurred: {e}")
