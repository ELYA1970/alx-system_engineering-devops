#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """return list containing titles of all hot articles"""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 50, "after": after, "count": count}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 404:
        return None
    response_ = response.json().get("data")
    after = response_.get("after")
    count += response_.get("dist")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
