from django.shortcuts import render,redirect
from .models import Category, Product
from django.db.models import Q
from.utils import calculate_discounted_price
from cart.views import cart_page
from .forms import SearchForm
from .models import Product, TV, AudioSystem, Laptop
from .forms import ProductSearchForm



'''
    # Get or create appliances category
    appliances_category, created = Category.objects.get_or_create(name='Garment Care', photo=None)

    # Check if air fryer already exists before creating it
    air_fryer, created = Product.objects.get_or_create(
        name='STEAM IRON',
        brand='PHILIPS',
        category=appliances_category,
        defaults={
            'photo': 'bg20.jpg',
            'price': 18540,
            'details': 'LED FLOODLIGHT 50W LED43/CW 4300 LUMEN GREY',
            'is_draft': False,
            'inventory': 125
        }
    )


    j=Product.objects.filter(id=)
    j.delete()

'''

def shop_page(request):

    products = Product.objects.filter(is_draft=False)
    categories = Category.objects.all()
    unique_category_names = []
    for category in categories:
        if category not in unique_category_names:
            unique_category_names.append(category.name)





    context = {
        'unique_category_names': set(unique_category_names),
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/shop.html', context)



def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    cart_data=cart_page(request)
    related_products = Product.objects.filter(category__name=product_details.category.name).exclude(id=product_id)
    context = {
        'product': product_details,
        'related_products': related_products,
        'cart_context': cart_data
    }
    return render(request, 'shop/product-details.html', context)


def discounted(request):
    product_ids=[11,1,19]

    products=Product.objects.filter(id__in=product_ids)

    discounted_prices=[]


    for product in products:
        discounted_price=calculate_discounted_price(product.price,20)
        discounted_prices.append(discounted_price)

    context= {
        'products': (products,discounted_prices)
    }    

    return render(request, 'shop/product-details.html', context)



def wishlist(request):
    return render(request, 'shop/wishlist.html')



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

    return render(request, 'shop/shop.html', context)

def search_products(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        product_type = form.cleaned_data.get('product_type')
        search_query = form.cleaned_data.get('search_query')

        if product_type:
            if product_type == 'TV':
                products = TV.objects.all()
            elif product_type == 'AudioSystem':
                products = AudioSystem.objects.all()
            elif product_type == 'Laptop':
                products = Laptop.objects.all()

        if search_query:
            products = products.filter(name__icontains=search_query)

    context = {
        'form': form,
        'products': products,
    }
    return render(request, 'search.html', context)



from .forms import TVForm,AudioForm

def add_tv(request):
    if request.method == 'POST':
        form = TVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tv_list')  # Replace with the appropriate view or URL name
    else:
        form = TVForm()
    return render(request, 'items/add_tv.html', {'form': form})


def tv_list(request):
    tvs = TV.objects.all()
    return render(request, 'items/tv_list.html', {'tvs': tvs})


def add_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio_list')  # Replace with the appropriate view or URL name
    else:
        form = AudioForm()
    return render(request, 'items/add_audio.html', {'form': form})


def audio_list(request):
    audios = AudioSystem.objects.all()
    return render(request, 'items/audio_list.html', {'audios': audios})

