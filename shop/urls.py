from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path(
        'product/<product_id>', views.product_details, name='product-details'),
    path('shop/<int:category_id>/', views.shop_page, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('search/', views.search_products, name='search_products'),
    path('add_item/', views.add_item ,name='add_item'),
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
    path('sony_tvs/', views.sony_tvs, name='sony_tvs'),
     path('hisense_tvs/', views.hisense_tvs, name='hisense_tvs'),

]
