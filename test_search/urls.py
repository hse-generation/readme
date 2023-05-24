from django.urls import path
from test_search import views

app_name = 'test_search'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_books/', views.search_books, name='search_books'),
]
