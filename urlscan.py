import requests
import argparse


urlscan_apikey = ""  # put urlscan api key here

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog="urlscan [-b] and [-d] or [-u]")
parser.add_argument("-b", type=str, default="", help="put brand")
parser.add_argument("-d", type=str, default="", help="put duration")
parser.add_argument("-q", type=str, default="", help="put custom query")
args = parser.parse_args()


def performSearch(brand, duration):
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
        return
    print(resp)


def performQuery(query):
    api_link = "https://urlscan.io/api/v1/search/"
    params = {
        "q": query
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
        return
    print(resp)


if __name__ == "__main__":
    if args.b:
        brand = args.b
        duration = args.d
        performSearch(brand, duration)
    elif args.q:
        performQuery(args.q)
    else:
        print(parser.print_help())
