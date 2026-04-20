import requests
import os

# 1. Setup API details
API_KEY = os.getenv('COINGECKO_API_KEY')
url = f"https://coingecko.com{API_KEY}"

# 2. Extract Data
response = requests.get(url)
price = response.json()['bitcoin']['usd']

# 3. If Analysis
print(f"Current Bitcoin Price: ${price}")
if price < 60000:
    print("ANALYSIS: Price is below target! Action required.")
else:
    print("ANALYSIS: Price is above target. No action needed.")
