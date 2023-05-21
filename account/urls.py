from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='account'),
    path('shelf/<int:status_id>', views.shelf, name='shelf'),
    path('logout/', views.logout, name='logout'),
]