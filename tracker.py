import requests
import os
from datetime import datetime

# 1. Setup API - Note the 'x_cg_demo_api_key' parameter
API_KEY = os.getenv('COINGECKO_API_KEY')
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
params = {
    'ids': 'bitcoin',
    'vs_currencies': 'usd',
    'x_cg_demo_api_key': API_KEY
}

try:
    # 2. Extract Data
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status() # This stops the script if the website is down
    data = response.json()
    
    price = data['bitcoin']['usd']
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 3. If Analysis & Note Recording
    status = "ACTION" if price < 60000 else "HOLD"
    note_entry = f"{now} | Price: ${price} | Status: {status}\n"

    with open("log.txt", "a") as f:
        f.write(note_entry)

    print(f"Success! Recorded: {note_entry}")

except Exception as e:
    print(f"Error occurred: {e}")
    exit(1) # Tells GitHub the job failed
