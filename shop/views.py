from django.shortcuts import render,redirect
from .models import Category, Product
from django.db.models import Q
from.utils import calculate_discounted_price

from .forms import SearchForm
from .models import Product, TV, AudioSystem, Laptop,Computer,Coffee_maker,Washing_machine
from .forms import ProductSearchForm,Form




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
    related_products = Product.objects.filter(category__name=product_details.category.name).exclude(id=product_id)
    context = {
        'product': product_details,
        'related_products': related_products,
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
            results = Product.objects.filter(Q(name__icontains=query)|Q(brand__icontains=query))

            
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



def add_item(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Replace with the appropriate view or URL name
    else:
        form = Form()
    return render(request, 'items/add_item.html', {'form': form})


def tv_list(request):
    tvs = TV.objects.filter(category__name='Televisions')
    return render(request, 'items/tv_list.html', {'tvs': tvs})

def sony_tvs(request):
    sonys=Product.objects.filter(brand='Sony',category__name='Televisions')
    
    return render(request, 'items/tvs/sony.html', {'sonys': sonys})

def hisense_tvs(request):
    hisenses=Product.objects.filter(brand='Hisense',category__name='Televisions') 
    
    return render(request, 'items/tvs/hisense.html', {'hisenses': hisenses})

def audio_list(request):
    audios = AudioSystem.objects.filter(category__name='Audio')
    return render(request, 'items/audio_list.html', {'audios': audios})

def computer_list(request):
    computers = Product.objects.filter(category__name='Computing')
    return render(request, 'items/computer_list.html', {'computers': computers})

def garmentcare_list(request):
    garments = Product.objects.filter(category__name='Garment Care')
    return render(request, 'items/computer_list.html', {'cares': cares})

def floorcare_list(request):
    floors = Product.objects.filter(category__name='Floor Care')
    return render(request, 'items/computer_list.html', {'floors': floors})

def kitchen(request):
    kitchens = Product.objects.filter(category__name='Floor Care')
    return render(request, 'items/computer_list.html', {'kitchens': kitchens})

def mobile_tablets(request):
    mbs = Product.objects.filter(category__name='Mobile&Tablets')
    return render(request, 'items/phones&tablets.html', {'mbs': mbs})

