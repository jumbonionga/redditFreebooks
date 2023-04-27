from fetchPosts import fetchPosts
from datetime import datetime
import json

posts = json.loads(fetchPosts())
for post in posts:
    if '&amp;' in post['title']:
        post['title'] = post['title'].replace('&amp;', '&')
    if '&amp;' in post['link_flair_text']:
        post['link_flair_text'] = post['link_flair_text'].replace('&amp;', '&')
    print(f"{post['title']} - {post['url_overridden_by_dest']}")
    print(f"created: {post['created']}")
    post['created'] = datetime.fromtimestamp(post['created']).date()
    print(f"created: {post['created']}")
