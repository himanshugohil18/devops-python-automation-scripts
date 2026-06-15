import requests

website = "https://google.com"

try:
    response = requests.get(website)

    if response.status_code == 200:
        print("Website is UP")
    else:
        print("Website is DOWN")

except:
    print("Website not reachable")