#!/usr/bin/python3

"""

this module contains a function that queries the Reddit API 
and prints the titles of the first 10 hot posts listed for a given subreddit.

"""

import requests


def top_ten(subreddit):
    """
        fetches the top 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Linux:MyRedditApp:1.0 (by /u/Few-Area5580)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for i in range(10):
            return data[i]["data"]["title"]
    else:
        return "None"
