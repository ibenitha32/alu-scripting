#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
        fetches the number of subscribers for a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Linux:MyRedditApp:1.0 (by /u/Few-Area5580)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    return 0
