from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after signup
            login(request, user)
            return redirect('index')  # Assuming 'index' is the name of the home page URL
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
