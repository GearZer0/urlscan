import requests
import argparse


urlscan_apikey = ""  # put urlscan api key here

# performs the parsing of the user given arguments
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter, prog="urlscan [-b] and [-d] or [-u]")
parser.add_argument("-b", type=str, default="", help="put brand")
parser.add_argument("-d", type=str, default="", help="put duration")
parser.add_argument("-q", type=str, default="", help="put custom query")
args = parser.parse_args()


# function to perform the fixed search based on brand and duration
def performSearch(brand, duration):
    api_link = "https://urlscan.io/api/v1/search/"
    # prepares the fixed query for a brand and duration provided
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
    # gets all the result set
    all_results = resp.get('results')
    print("Total: {}".format(resp.get('total')))
    print("Took: {}".format(resp.get('took')))
    print("Has More: {}".format(resp.get('has_more')))
    print('\n')
    for result in all_results:
        print("brand")
        print("-----")
        # gets all the brand list
        all_brands = result.get('brand')
        for brand_data in all_brands:
            print("Name: {}".format(brand_data.get('name')))
            print("Country: {}".format(",".join(brand_data.get('country'))))
            print("Vertical: {}".format(",".join(brand_data.get('vertical'))))
            print("Key: {}".format(brand_data.get('key')))
        print("Result: {}".format(result.get('result')))
        print("Screenshot: {}".format(result.get('screenshot')))
        print("task")
        print("----")
        print("URL: {}".format(result.get('task').get('url')))
        print("Domain: {}".format(result.get('task').get('domain')))
        print("Time: {}".format(result.get('task').get('time')))
        print("page")
        print("-----")
        print("URL: {}".format(result.get('page').get('url')))
        print("Domain: {}".format(result.get('page').get('domain')))
        print("Status: {}".format(result.get('page').get('status')))
        print("Server: {}".format(result.get('page').get('server')))
        print("IP: {}".format(result.get('page').get('ip')))
        print("="*20)


# function to perform custom search query based on user input
def performQuery(query):
    api_link = "https://urlscan.io/api/v1/search/"
    # prepares custom query parameters
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
    # gets all the result set
    all_results = resp.get('results')
    print("Total: {}".format(resp.get('total')))
    print("Took: {}".format(resp.get('took')))
    print("Has More: {}".format(resp.get('has_more')))
    for result in all_results:
        print("brand")
        print("-----")
        # gets all the brand list
        all_brands = result.get('brand')
        for brand_data in all_brands:
            print("Name: {}".format(brand_data.get('name')))
            print("Country: {}".format(",".join(brand_data.get('country'))))
            print("Vertical: {}".format(",".join(brand_data.get('vertical'))))
            print("Key: {}".format(brand_data.get('key')))
        print("Result: {}".format(result.get('result')))
        print("Screenshot: {}".format(result.get('screenshot')))
        print("task")
        print("----")
        print("URL: {}".format(result.get('task').get('url')))
        print("Domain: {}".format(result.get('task').get('domain')))
        print("Time: {}".format(result.get('task').get('time')))
        print("page")
        print("-----")
        print("URL: {}".format(result.get('page').get('url')))
        print("Domain: {}".format(result.get('page').get('domain')))
        print("Status: {}".format(result.get('page').get('status')))
        print("Server: {}".format(result.get('page').get('server')))
        print("IP: {}".format(result.get('page').get('ip')))
        print("="*20)


if __name__ == "__main__":
    # checks whether the input argument is a brand
    if args.b:
        brand = args.b
        duration = args.d
        performSearch(brand, duration)
    # checks whether the input argument is a custom query
    elif args.q:
        performQuery(args.q)
    else:
        # detects that no or invalid arguments given, guides the user on what to do
        print(parser.print_help())
