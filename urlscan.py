import requests


urlscan_apikey = ""  # put urlscan api key here

brand = input("Enter brand: ")
duration = input("Enter duration: ")


def performSearch():
    api_link = "https://urlscan.io/api/v1/search/"
    params = {
        "q": "brand.key:{} AND date:>now-{}".format(brand, duration)
    }
    headers = {
        "Content-Type": "application/json",
        "API-Key": urlscan_apikey,
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = requests.get(api_link, headers=headers, params=params).json()
    except:
        print("Failed to open {}".format(api_link))
    print(resp)

if __name__ == "__main__":
    performSearch()
