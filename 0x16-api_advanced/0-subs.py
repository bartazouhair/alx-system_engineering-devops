#!/usr/bin/python3
"""
    Uses reddit API print number of subscribers of a subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Get numbers of subscribers by given"""
    url_sred_inf = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url_sred_inf, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    r_json = response.json()
    num_subs = r_json.get("data").get("subscribers")
    return num_subs
