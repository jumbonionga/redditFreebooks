from django.http import HttpResponse
from django.shortcuts import render
from fetchPosts import fetchPosts
from datetime import datetime
import json

# Create your views here.


def home(request):
    # Fetch books
    books = json.loads(fetchPosts())

    for book in books:
        # Change 'created' to actual date format from epoch
        book['created'] = datetime.fromtimestamp(book['created']).date()

        # Replace '&amp;' to '&' in title
        if '&amp;' in book['title']:
            book['title'] = book['title'].replace('&amp;', '&')

        # Replace '&amp;' to '&' in link_flair_text
        if '&amp;' in book['link_flair_text']:
            book['link_flair_text'] = book['link_flair_text'].replace(
                '&amp;', '&')

    return render(request, 'books.html', {
        'books': books
    })
