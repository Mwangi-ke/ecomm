from django.shortcuts import render
from .models import Category, Product
from django.db.models import Q
from.utils import calculate_discounted_price


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
        'related_products': related_products
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






