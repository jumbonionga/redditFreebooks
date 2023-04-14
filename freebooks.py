from fetchPosts import fetchPosts
import json

posts = json.loads(fetchPosts())
for post in posts:
    print(f"{post['title']} - {post['url_overridden_by_dest']}")
