#Importing and getting keys
import os
from dotenv import load_dotenv
import requests
load_dotenv()
api_key = os.getenv("API_KEY")

#Testing API connection
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GOOGL&apikey={api_key}'
req = requests.get(url)
data = req.json()
print(data)