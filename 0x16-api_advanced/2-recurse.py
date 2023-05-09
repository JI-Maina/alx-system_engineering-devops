#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """queries the Reddit API
    
    args:
        subreddit - subreddit name

    returns a list containing the titles of all hot articles for a given
    subreddit"""
    global after
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': 'Title/0.1 by JI-Maina'}
    param = {'after': after}

    res = requests.get(
            url, headers=header, params=param, allow_redirects=False)

    if res.status_code == 200:
        next = res.json().get('data').get('after')
        if next is None:
            after = next
            recurse(subreddit, hot_list)
        list_titles = res.json().get('data').get('children')
        for title in list_titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
