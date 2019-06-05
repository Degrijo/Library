from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import BookForm
from .models import Book


def view_user_page(request, pk):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = User.objects.all().get(id=pk)
            book.save()
    return render(request, 'user_page/user_page.html',
                  {'Book': User.objects.all().get(id=pk).book_set.all(), 'form': BookForm()})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('../')
    else:
        form = BookForm(instance=book)
    return render(request, 'user_page/edit_book.html', {'form': form})
