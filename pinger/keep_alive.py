import time
import requests

url = "https://svaravarna-search.onrender.com"

while True:
    try:
        response = requests.get(url)
        print(f"Pinged {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")
    # Wait 600 seconds (10 minutes)
    time.sleep(600)
