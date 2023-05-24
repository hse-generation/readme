from django.shortcuts import render
from books.models import Books
from authors.models import Authors
from genres.models import Genres


def index(request):
    return render(request, 'test_search/index.html')


from django.shortcuts import render
from books.models import Books
from authors.models import Authors
from genres.models import Genres


def index(request):
    return render(request, 'test_search/index.html')

def search_books(request):
    if request.method == 'POST':
        query = request.POST.get('book_name', '')
        ans = Books.search(query)
        return render(request, 'search_books.html', {'ans': ans})
