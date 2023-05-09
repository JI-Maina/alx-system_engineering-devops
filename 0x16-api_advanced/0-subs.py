#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API
    
    args: subreddit - subreddit name
    
    returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "ChangeMeClient/0.1 by Makaburi_McMaina"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return(res.json().get('data').get('subscribers'))
    return 0
