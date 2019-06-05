from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User


def view_main_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main_page/main_page.html', {'form': UserForm(), 'User': User.objects.all()})
