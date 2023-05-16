from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('book/<int:book_id>',views.book_by_id, name = 'book by ID'),
    path('allbooks', views.show_all_books, name = 'show all books'),
]