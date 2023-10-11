#!/usr/bin/python3#!/usr/bin/python3
"""
Queries the Reddit API and parse titles of hot articles
"""
import requests


def count_words(subreddit, word_list, after=None, count_list=None):

    """
    Prints a sorted count of a given keyword delimited by spaces
    in the title of the hot article
    Args:
        subreddit (str): subreddit of the Reddit API
        word_list (list): list of keywords to search for
    """

    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko)"

    headers = {
            "User-Agent": user_agent
            }

    if count_list is None:
        count_list = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200 or 'data' not in response.json():
        return None

    r = response.json()
    after = r.get("data").get("after")
    posts = r.get("data").get("children")

    for post in posts:
        title = post.get("data").get("title")
        title_words = title.lower().split()
        for word in word_list:
            w = word.lower()
            if w in title_words:
                if w in count_list:
                    count_list[w] += title_words.count(w)
                else:
                    count_list[w] = title_words.count(w)

    if after is None:
        sort_count = sorted(count_list.items(), key=lambda k: (-k[1], k[0]))
        for count in sort_count:
            print("{} {}".format(count[0], count[1]))
    else:
        return count_words(subreddit, word_list, after, count_list)
