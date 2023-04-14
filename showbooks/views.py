from django.http import HttpResponse
from django.shortcuts import render
from fetchPosts import fetchPosts
import json

# Create your views here.


def home(request):
    books = json.loads(fetchPosts())
    return render(request, 'books.html', {
        'books': books
    })
