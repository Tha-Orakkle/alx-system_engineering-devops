#!/usr/bin/python3
"""
Queries the Reddit API to get the list containing titles of hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of hot articles
    Args:
        subreddit (str): subreddit of the Reddit API
        hot_listt (list): list of hot articles
    Return:
        hot_list or None if subreddit is invalid
    """

    if after is None:
        return hot_list

    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, after)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko)"

    headers = {
            "User-Agent": user_agent
            }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200 or 'data' not in response.json():
        return None
    else:
        r = response.json()
        after = r.get("data").get("after")
        posts = r.get("data").get("children")
        for post in posts:
            title = post.get("data").get("title")
            hot_list.append(title)

    return recurse(subreddit, hot_list, after)
