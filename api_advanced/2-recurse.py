#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Linux:MyRedditApp:1.0 (by /u/Few-Area5580)"
    }
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()["data"]
    hot_posts = data["children"]
    after = data["after"]

    for post in hot_posts:
        hot_list.append(post["data"]["title"])

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
