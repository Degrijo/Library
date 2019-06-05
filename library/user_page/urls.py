from django.urls import path
from .views import view_user_page, edit_book

urlpatterns = [
    path('', view_user_page, name='view_user_page'),
    path('<int:pk>/', edit_book, name='edit_book')
]
