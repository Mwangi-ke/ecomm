from django.shortcuts import render
from shop.models import Product
from contact.forms import SubscriberForm
from .forms import SearchForm


def home_page(request):
    products = Product.objects.all()[:12]
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'products': products,
        'forms': forms
    }
    return render(request, 'home.html', context)


def search(request):
    query = None
    results = []
    form = SearchForm()

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(f"Search query: {query}")  # Debugging print statement
            results = Product.objects.filter(name__icontains=query)
            print(f"Search results: {results}")  # Debugging print statement
        else:
            print("Form is not valid")  # Debugging print statement
            print(form.errors)  # Debugging print statement

    context = {
        'form': form,
        'query': query,
        'results': results
    }

    return render(request, 'new.html', context)
