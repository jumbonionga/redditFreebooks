"""
fetchPosts
Retrieve all NEW posts in the subreddit and filter out the 'EXPIRED' ones.

Returns the list as JSON
"""
import requests
import requests.auth
import json
import time
from datetime import datetime, timedelta


def fetchPosts():
    '''
    Fetch the NEW 1000 posts on r/freeebooks in the MONTH
    '''

    filtered_posts = []
    posts = []
    base_url = 'https://www.reddit.com/r/freeebooks/new.json?limit=1000&t=month'

    def makerequest(url):
        # Make request
        try:
            request = requests.get(
                url, headers={'User-agent': 'curatedFreebooks'})
        except:
            print("An error occurred")

        # Add requests to posts
        for entry in request.json()["data"]["children"]:
            posts.append(entry)

        # Check if last children is <= 1 day
        elements = len(request.json()["data"]["children"])
        lastCreated = request.json(
        )["data"]["children"][elements-1]["data"]["created"]
        dateCreated = datetime.fromtimestamp(lastCreated).date()
        today = datetime.now().date()
        oneDay = timedelta(days=1)
        if (today-dateCreated > oneDay):
            for entry in posts:
                if entry["data"]["link_flair_text"] != "Expired":
                    filtered_posts.append(entry["data"])
            # filtered_posts = [
            #     post['data'] for post in posts if post['data']['link_flair_text'] != 'Expired']
        else:
            nextPage = request.json()["data"]["after"]
            newURL = base_url + '&after='+nextPage
            return makerequest(newURL)

    makerequest(base_url)
    return json.dumps(filtered_posts)
