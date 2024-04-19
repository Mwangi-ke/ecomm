from django.shortcuts import render
from .models import Category, Product


'''
    # Get or create appliances category
    appliances_category, created = Category.objects.get_or_create(name='switches', photo=None)

    # Check if air fryer already exists before creating it
    air_fryer, created = Product.objects.get_or_create(
        name='1gang 1way switch',
        brand='HIMEL'
        category=appliances_category,
        defaults={
            'photo': '1g 1w.jpg',
            'price': 2000,
            'details': ' HWDPS1G1W  1 gang 1 way switch',
            'is_draft': False,
            'inventory': 625
        }
    )
'''

def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter(is_draft=False)


    

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/shop.html', context)



def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category=product_details.category)
    context = {
        'product': product_details,
        'related_products': related_products
    }
    return render(request, 'shop/product-details.html', context)







def wishlist(request):
    return render(request, 'shop/wishlist.html')






