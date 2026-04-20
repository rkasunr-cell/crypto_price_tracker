import requests
import os
from datetime import datetime

# 1. Setup API
API_KEY = os.getenv('COINGECKO_API_KEY')
url = f"https://coingecko.com{API_KEY}"

# 2. Extract Data
response = requests.get(url)
price = response.json()['bitcoin']['usd']
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. If Analysis & Note Recording
status = "ACTION" if price < 60000 else "HOLD"
note_entry = f"{now} | Price: ${price} | Status: {status}\n"

# 4. Save to a local file
with open("log.txt", "a") as f:
    f.write(note_entry)

print(f"Recorded: {note_entry}")

