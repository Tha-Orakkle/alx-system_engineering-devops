#!/usr/bin/python3
"""Function that queries a Reddit API"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    or None if subreddit is invlid
    Args:
        subreddit: (str)"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko)"
    headers = {
            "User-Agent": user_agent
            }
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        if (len(posts) > 0):
            for post in posts:
                print(post.get("data").get("title"))
        else:
            print(None)
    print(None)
