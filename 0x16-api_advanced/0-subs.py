#!/usr/bin/python3
"""Function that queries a Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit
    or returns 0 if subreddit is invlid
    Args:
        subreddit: (str)"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko)"
    headers = {
            "User-Agent": user_agent
            }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
