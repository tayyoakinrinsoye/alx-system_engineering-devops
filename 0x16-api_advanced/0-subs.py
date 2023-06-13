#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)

    if response.status.code == 200
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
