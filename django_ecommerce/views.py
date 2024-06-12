from django.shortcuts import render
from shop.models import Product
from contact.forms import SubscriberForm
from .forms import SearchForm
from django.db.models import Q


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
            results = Product.objects.filter(Q(name__icontains=query)|Q(brand__icontains=query))

            
    context = {
        'form': form,
        'query': query,
        'results': results
    }

    return render(request, 'new.html', context)




    
