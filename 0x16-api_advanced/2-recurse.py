#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/114.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]

        if after is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
