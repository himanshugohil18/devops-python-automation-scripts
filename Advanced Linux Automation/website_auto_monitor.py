import requests
import time

website = "https://google.com"

while True:
    try:
        response = requests.get(website)

        if response.status_code == 200:
            print("Website UP")

        else:
            print("Website DOWN")

    except:
        print("Website unreachable")

    time.sleep(30)