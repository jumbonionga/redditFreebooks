"""
fetchPosts
Retrieve all NEW posts in the subreddit and filter out the 'EXPIRED' ones.

Returns the list as JSON
"""
import requests
import requests.auth
import json


def fetchPosts():
    '''
    Fetch the NEW 1000 posts on r/freeebooks in the MONTH
    '''

    filtered_posts = []

    try:
        base_url = 'https://www.reddit.com/r/freeebooks/new.json?limit=1000&t=month'
        request = requests.get(
            base_url, headers={'User-agent': 'curatedFreebooks'})
    except:
        print("An error occurred")

    posts = request.json()

    filtered_posts = [post['data'] for post in posts['data']
                      ['children'] if post['data']['link_flair_text'] != 'Expired']

    return json.dumps(filtered_posts)
