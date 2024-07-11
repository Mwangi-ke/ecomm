from django.shortcuts import render,redirect,get_object_or_404
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
 
    for product in related_products:
        product.new_price= product.price * 1.1
        
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




def sort_products_view(request):
    sort_by = request.GET.get('sort_by', 'name')  # Default to sorting by name if no criteria is provided
    price_range = request.GET.get('price_range', 'all')  # Default to 'all' if no price range is provided
    products = Product.sort_products(sort_by=sort_by, price_range=price_range)
    return render(request, 'shop/sorted_products.html', {'products': products})





def add_item(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')  # Replace with the appropriate view or URL name
    else:
        form = Form()
    return render(request, 'items/add_item.html', {'form': form})



 # TELEVISIONS

def all_brands(request):
    
    products = Product.objects.filter(category__name='Televisions')
    brands = products.values_list('brand', flat=True).distinct()
    
    # Create a mapping of brands to logo filenames
    brand_logos = {
        'Sony': 'sony_logo.png',
        'Hisense': 'hisense_logo.png',
        # Add more brand logos here
    }

    context = {
        'brands': brands,
        'brand_logos': brand_logos
    }
    return render(request,'items/tvs/all_brands.html',context)



def tv_list(request):
    tvs = Product.objects.filter(category__name='Televisions')
    return render(request, 'items/tv_list.html', {'tvs': tvs})

def sony_tvs(request):
    sonys=Product.objects.filter(brand='Sony',category__name='Televisions')    
    return render(request, 'items/tvs/sony.html', {'sonys': sonys})

def hisense_tvs(request):
    hisenses=Product.objects.filter(brand='Hisense',category__name='Televisions')  
    return render(request, 'items/tvs/hisense.html', {'hisenses': hisenses})

def lg_tvs(request):
    lgs=Product.objects.filter(brand='LG',category__name='Televisions') 
    
    return render(request, 'items/tvs/lg.html', {'lgs': lgs})

def tlc_tvs(request):
    tlcs=Product.objects.filter(brand='TLC',category__name='Televisions') 
    
    return render(request, 'items/tvs/tcl.html', {'tlcs': tlcs})

def skyworth_tvs(request):
    skys=Product.objects.filter(brand='Skyworth',category__name='Televisions') 
    
    return render(request, 'items/tvs/hisense.html', {'skys': skys})

def vitron_tvs(request):
    vitrons=Product.objects.filter(brand='Vitrons',category__name='vitrons')  
    return render(request, 'items/tvs/hisense.html', {'vitrons': vitrons})




# AUDIO SYSTEMS

def audio_list(request):
    audios = Product.objects.filter(category__name='Audio')
    return render(request, 'items/audios/audio_list.html', {'audios': audios})

def soundbars(request):
    sbars=Product.objects.filter(category__name='Audio', subcategory='soundbars')
    return render(request,'items/audios/sounbars.html',{'sbars':sbars})


def hometheatres(request):
    htheatres=Product.objects.filter(category__name='Audio', subcategory='hometheatres')
    return render(request,'items/audios/hometheatres.html',{'htheatres':htheatres})


def hifisystems(request):
    hifis=Product.objects.filter(category__name='Audio', subcategory='hifi systems')
    return render(request,'items/audios/hifisystems.html',{'hifis':hifis})


def headphones(request):
    phones=Product.objects.filter(category__name='Audio', subcategory='head/ear phones')
    return render(request,'items/audios/headphones.html',{'phones':phones})


def subwoofers(request):
    woofers=Product.objects.filter(category__name='Audio', subcategory='subwoofers')
    return render(request,'items/audios/woofers.html',{'woofers':woofers})



 # COMPUTING

def all_in_one(request):
   all_in_ones=Product.objects.filter(category__name='Destops')
   return render(request,'items/computing/all_in_one.html',{'all_in_ones':all_in_ones}) 


def desktop(request):
   desktops=Product.objects.filter(category__name='Destops')
   return render(request,'items/computing/desktop.html',{'desktops':desktops})


def computer_accessories(request):
   accessories=Product.objects.filter(category__name='Computer_accessories')
   return render(request,'items/computing/computing_accessories.html',{'accessories':accessories})

 # Laptops

def laptops(request):
    laptop=Product.objects.filter(category__name='Laptops')
    return render(request,'items/laptops/laptops.html',{'laptop':laptop})

def hp_laptops(request):
    hps=Product.objects.filter(brand='HP',category__name='Laptops')
    return render(request, 'items/laptops/hp.html', {'hps': hps})

def dell_laptops(request):
    dells=Product.objects.filter(brand='DELL',category__name='Laptops')
    return render(request, 'items/laptops/dell.html', {'dells': dells})


def Mac_laptops(request):
    macs=Product.objects.filter(brand='MAC',category__name='Laptops')
    return render(request, 'items/laptops/mac.html', {'macs': macs})


def asus_laptops(request):
    asuses=Product.objects.filter(brand='ASUS',category__name='Laptops')
    return render(request, 'items/laptops/asus.html', {'asuses': asuses})


def lenovo_laptops(request):
    lenovos=Product.objects.filter(brand='LENOVO',category__name='Laptops')
    return render(request, 'items/laptops/lenovo.html', {'lenovos': lenovos})


def computer_list(request):
    computers = Product.objects.filter(category__name='Computing')
    return render(request, 'items/computer_list.html', {'computers': computers})





# Mobiles & Tablets

def mobile_tablets(request):
    mbs = Product.objects.filter(category__name='Mobile&Tablets')
    return render(request, 'items/phones&tablets.html', {'mbs': mbs})


def samsung_phones(request):
    samsungs=Product.objects.filter(brand='SAMSUNG',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/samsungs.html', {'samsungs':samsungs})


def i_phones(request):
    iphones=Product.objects.filter(brand='IPHONE',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/iphones.html', {'iphones':iphones})


def oneplus_phones(request):
    ones=Product.objects.filter(brand='ONEPLUS',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/oneplus.html', {'ones':ones})


def oppo_phones(request):
    oppos=Product.objects.filter(brand='OPPO',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/oppos.html', {'oppos':oppos})


def xiaomi_phones(request):
    xiaomis=Product.objects.filter(brand='XIAOMI',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/xiaomis.html', {'xiaomis':xiaomis})

def realme_phones(request):
    realmes=Product.objects.filter(brand='REALME',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/realmes.html', {'realmes':realmes})


def huawei_phones(request):
    huaweis=Product.objects.filter(brand='HUAWEI',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/huaweis.html', {'huaweis':huaweis})


def nokia_phones(request):
    nokias=Product.objects.filter(brand='NOKIA',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/nokias.html', {'nokias':nokias})


def vivo_phones(request):
    vivos=Product.objects.filter(brand='VIVO',category__name='Mobile&Tablets',subcategory__name='Phones')
    return render(request, 'items/mob&tabs/vivos.html', {'vivos':vivos})



# HOME & LIVING

def floorcare_list(request):
    floors = Product.objects.filter(category__name='Floor Care')
    return render(request, 'items/floor_care.html', {'floors': floors})

def kitchen(request):
    kitchens = Product.objects.filter(category__name='Floor Care')
    return render(request, 'items/kitchen.html', {'kitchens': kitchens})

def fridges(request):
    fridges = Product.objects.filter(category__name='Home&living', subcategory= 'fridges')
    return render(request, 'items/home&living/fridges.html', {'fridges': fridges})

def freezers(request):
    freezers = Product.objects.filter(category__name='Home&living', subcategory= 'freezers')
    return render(request, 'items/home&living/freezers.html', {'fridges': fridges})


def cookers(request):
    cookers = Product.objects.filter(category__name='Home&living', subcategory= 'cookers')
    return render(request, 'items/home&living/cookers.html', {'cookers': cookers})




def washing_machines(request):
    washings = Product.objects.filter(category__name='Home&living', subcategory= 'washing machines')
    return render(request, 'items/home&living/washing.html', {'washings': washings})


def water_dispensers(request):
    dispensers = Product.objects.filter(category__name='Home&living', subcategory= 'dispensers')
    return render(request, 'items/home&living/dispensers.html', {'dispensers': dispensers})


def vacuum_cleaners(request):
    vacuums = Product.objects.filter(category__name='Home&living', subcategory= 'vacuum_cleaners')
    return render(request, 'items/home&living/vacuums.html', {'vacuums': vacuums})

def air_fryers(request):
    fryers = Product.objects.filter(category__name='Home&living', subcategory= 'air_fryers')
    return render(request, 'items/home&living/airfryers.html', {'fryers': fryers})

def blenders(request):
    blenders = Product.objects.filter(category__name='Home&living', subcategory= 'blenders')
    return render(request, 'items/home&living/blenders.html', {'blenders': blenders})


def juicers(request):
    juicers = Product.objects.filter(category__name='Home&living', subcategory= 'juicers')
    return render(request, 'items/home&living/juicers.html', {'juicers': juicers})

def toasters(request):
    toasters = Product.objects.filter(category__name='Home&living', subcategory= 'toasters')
    return render(request, 'items/home&living/toasters.html', {'toasters': toasters})

def kettles(request):
    kettles = Product.objects.filter(category__name='Home&living', subcategory= 'electric_kettles')
    return render(request, 'items/home&living/kettles.html', {'kettles': kettles})

def coffee_makers(request):
    coffees = Product.objects.filter(category__name='Home&living', subcategory= 'coffee_makers')
    return render(request, 'items/home&living/coffees.html', {'coffees': coffees})

def food_processors(request):
    processors = Product.objects.filter(category__name='Home&living', subcategory= 'processors')
    return render(request, 'items/home&living/processors.html', {'processors': processors})


# Garment Care

def garmentcare_list(request):
    cares = Product.objects.filter(category__name='Garment Care')
    return render(request, 'items/garment_care.html', {'cares': cares})


def iron_boxes(request):
    irons = Product.objects.filter(category__name='Home&living', subcategory= 'iron_boxes')
    return render(request, 'items/garment_care/irons.html', {'irons':irons})



 # Waste management

def dustbins(request):
    bins = Product.objects.filter(category__name='Home&living', subcategory= 'bins')
    return render(request, 'items/home&living/bins.html', {'bins': bins}) 



 # Personal Care

def female_grooming(request):
    females = Product.objects.filter(category__name='Personal care', subcategory = 'female grooming')
    return render(request, 'items/female_grooming.html', {'females': females})


def male_grooming(request):
    males = Product.objects.filter(category__name='Personal care', subcategory = 'male grooming')
    return render(request, 'items/male_grooming.html', {'males': males})


def dryers_straighteners(request):
    dryers = Product.objects.filter(category__name='Personal care', subcategory = 'dryers&straighteners')
    return render(request, 'items/dryers_straighteners.html', {'dryers': dryers})


def toothbrush(request):
    brushes = Product.objects.filter(category__name='Personal care', subcategory = 'toothbrush')
    return render(request, 'items/toothbrush.html', {'brushes': brushes})



# Gaming

def ps5(request):
    ps5s=Product.objects.filter(category_name='Gaming', subcategory='playstations')
    return render(request,'items/gaming/playtations.html', {'ps5sp':ps5s})

def play_station_consoles(request):
    playstation_consoles = Product.objects.filter(category__name='Gaming', subcategory = 'playstation consoles')
    return render(request, 'items/playstationconsoles.html', {'playstation_consoles': playstation_consoles})


def xbox_consoles(request):
    xbox_consoles = Product.objects.filter(category__name='Gaming', subcategory = 'xbox consoles')
    return render(request, 'items/xboxconsoles.html', {'playstation_consoles': xbox_consoles})

def gaming_controllers(request):
    controllers = Product.objects.filter(category__name='Gaming', subcategory = 'gaming_controllers')
    return render(request, 'items/gaming_controllers.html.html', {'controllers': controllers})




def category_view(request,category_name):
    categorys=get_object_or_404(Category,name=category_name)
    products=Product.objects.filter(category=categorys)
    return render(request,'shop/shop.html',{'category':categorys,'products':products})