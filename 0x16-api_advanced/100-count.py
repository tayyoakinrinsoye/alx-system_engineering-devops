#!/usr/bin/python3
"""count words function"""

import requests


def count_words(subreddit, word_list, count_dict={}):
    if not word_list:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    keyword = word_list[0].lower()
    if keyword in count_dict:
        count_dict[keyword] += 1
    else:
        count_dict[keyword] = 1

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    # Set a custom User-Agent header
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/114.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in title.split():
                if word.rstrip('.!_') == keyword:
                    count_dict[keyword] += 1

        after = data["data"]["after"]

        if after is not None:
            return count_words(subreddit, word_list, count_dict=count_dict)
        else:
            return count_words(subreddit, word_list[1:], count_dict=count_dict)
    else:
        return
