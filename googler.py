import os
import json
import argparse
import requests

config_path = os.path.join(os.path.dirname(__file__), "config.json") # config file location

def save_api_key(api_key):
    with open(config_path, "w") as conf_file:
        json.dump({"api_key": api_key}, conf_file)
    
def load_api_key():
    if os.path.exists(config_path): # load from config file if existent
        with open(config_path, "r") as conf_file:
            return json.load(conf_file).get("api_key") # retrieve API key
    else:
        return None

def google_search(query, api_key, num=5):
    endpoint = "https://serpapi.com/search" # query SerpAPI endpoint
    params = {
        "engine":"google",
        "q" : query,
        "num" : num,
        "api_key" : api_key,
    }

    response = requests.get(endpoint, params=params) # request endpoint
    
    data = response.json()
    results = data.get("organic_results", []) # organic results are the standard google results
    
    for i in range(len(results)):
        print(f"{i+1}. {results[i]['title']}") # numbered list of title and link on new line
        print(f"Link: {results[i]['link']}")
        print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Google Search using SerpAPI")
    parser.add_argument("-q", "--query", type=str, help="Search query")
    parser.add_argument("-n", "--num", type=int, help="Number of results shown. Default is 5")
    parser.add_argument("--set-key", type=str, help="set API key, creates JSON file") 

    args = parser.parse_args()

    if args.set_key:
        save_api_key(args.set_key)
        print("API key saved")
    else:
        api_key = load_api_key()
        if not api_key: # no API key loaded
            print("Please obtain API key from https://serpapi.com and load it using --set-key")
        else:
            google_search(args.query, api_key, args.num)