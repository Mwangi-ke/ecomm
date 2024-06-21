from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('product/<product_id>', views.product_details, name='product-details'),
    path('shop/<int:category_id>/', views.shop_page, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('search/', views.search_products, name='search_products'),
    path('add_item/', views.add_item ,name='add_item'),
    path('sort-products/', views.sort_products_view, name='sort_products'),
    path('all_brands/', views.all_brands ,name='all_brands'),
    path('tv_list/', views.tv_list, name='tv_list'),
    path('audio_list/', views.audio_list, name='audio_list'),
    path('computing_list/', views.computer_list, name='computing_list'),
    path('phone&tablet_list/', views.tv_list, name='phone&tablet_list'),
    path('refrigerator_list/', views.tv_list, name='refrigerator_list'),
    path('laptop_list/', views.tv_list, name='laptop_list'),
    path('washing_list/', views.tv_list, name='washing_list'),
    path('blender_list/', views.tv_list, name='blender_list'),
    path('coffee_list/', views.tv_list, name='coffee_list'),



    # TV brands
    path('sony_tvs/', views.sony_tvs, name='sony_tvs'),
    path('hisense_tvs/', views.hisense_tvs, name='hisense_tvs'),
    path('lg_tvs/', views.lg_tvs, name='lg_tvs'),
    path('tlc_tvs/', views.tlc_tvs, name='tlc_tvs'),
    path('skyworth_tvs/', views.skyworth_tvs, name='skyworth_tvs'),
    path('vitron_tvs/', views.vitron_tvs, name='vitron_tvs'),

    # Audio systems
    path('soundbars/', views.soundbars, name='soundbars'),
    path('hometheatres/', views.hometheatres, name='hometheatres'),
    path('hifisystems/', views.hifisystems, name='hifisystems'),
    path('headphones/', views.headphones, name='headphones'),
    path('subwoofers/', views.subwoofers, name='subwoofers'),

    # Laptops
    path('laptops/', views.laptops, name='laptops'),
    path('hp_laptops/', views.hp_laptops, name='hp_laptops'),
    path('dell_laptops/', views.dell_laptops, name='dell_laptops'),
    path('mac_laptops/', views.Mac_laptops, name='mac_laptops'),
    path('asus_laptops/', views.asus_laptops, name='asus_laptops'),
    path('lenovo_laptops/', views.lenovo_laptops, name='lenovo_laptops'),


    # Computing
    path('all_in_one/', views.all_in_one, name='all_in_one'),
    path('desktops/', views.desktop, name='desktops'),
    path('computer_accessories/', views.computer_accessories, name='computer_accessories'),

    # Mobile & Tablets
    path('tablets/', views.mobile_tablets, name='tablets'),
    path('samsung_phones/', views.samsung_phones, name='samsung'),
    path('i_phones/', views.i_phones, name='i_phones'),
    path('oneplus_phones/', views.oneplus_phones, name='oneplus'),
    path('oppo_phones/', views.oppo_phones, name='oppo'),
    path('xiaomi_phones/', views.xiaomi_phones, name='xiaomi'),
    path('huawei_phones/', views.huawei_phones, name='huawei'),
    path('nokia_phones/', views.nokia_phones, name='nokia'),
    path('vivo_phones/', views.vivo_phones, name='vivo'),
    path('realme_phones/', views.realme_phones, name='realme'),

    # Home & Living
    path('floorcare_list/', views.floorcare_list, name='floorcare_list'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('fridges/', views.fridges, name='fridges'),
    path('freezers/', views.freezers, name='freezers'),
    path('washing_machines/', views.washing_machines, name='washing_machines'),
    path('water_dispensers/', views.water_dispensers, name='water_dispensers'),
    path('vacuum_cleaners/', views.vacuum_cleaners, name='vacuum_cleaners'),
    path('airfryers/', views.air_fryers, name='airfryers'),
    path('blenders/', views.blenders, name='blenders'),
    path('juicers/', views.juicers, name='juicers'),
    path('toasters/', views.toasters, name='toasters'),
    path('kettles/', views.kettles, name='electric_kettles'),
    path('coffee_makers/', views.coffee_makers, name='coffee_makers'),
    path('cookers/', views.cookers, name='cookers'),
    path('food_processors/', views.food_processors, name='food_processors'),

    # Garment Care
    path('garmentcare_list/', views.garmentcare_list, name='garmentcare_list'),
    path('iron_boxes/', views.iron_boxes, name='iron_boxes'),

    # Waste Management
    path('dustbins/', views.dustbins, name='dustbin'),

    # Personal Care
    path('female_grooming/', views.female_grooming, name='female_grooming'),
    path('male_grooming/', views.male_grooming, name='male_grooming'),
    path('dryers_straighteners/', views.dryers_straighteners, name='dryers'),
    path('toothbrush/', views.toothbrush, name='toothbrush'),

    # Gaming
    path('ps5/', views.ps5, name='ps5'),
    path('play_station_consoles/', views.play_station_consoles, name='play_station_consoles'),
    path('xbox_consoles/', views.xbox_consoles, name='xbox_consoles'),
    path('gaming_controllers/', views.gaming_controllers, name='gaming_controllers'),
]


