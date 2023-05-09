#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts

    args:
        subreddit - subreddit name
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "ChangeMeClient/0.1 by Makaburi_McMaina"}

    res = requests.get(
            url, headers=headers, allow_redirects=False,
            params={'limit': '10'})

    if res.status_code == 200:
        posts = res.json()
        for post in posts['data']['children']:
            print(post['data']['title'])
    print(None)
