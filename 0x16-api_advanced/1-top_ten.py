#!/usr/bin/python3
"""Function to print top 10 hot posts on a given Reddit subreddit"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print("None")
