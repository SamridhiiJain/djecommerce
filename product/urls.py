
from django.urls import path
from .views import *

urlpatterns = [
    # category
    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/edit/<slug:slug>/', category_edit, name='category_edit'),
    path('category/delete/<slug:slug>/', category_delete, name='category_delete'),

    # product
    path('products/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/edit/<slug:slug>/', product_edit, name='product_edit'),
    path('product/delete/<slug:slug>/', product_delete, name='product_delete'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:category_slug>/products', category_product_list, name='product_list_by_category'),
    path('search/', search, name='search'),


     ############# wishlist
    path('wishlist/', product_wishlist, name='wishlist'),
    path('wishlist/add/<slug:slug>/', wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<slug:slug>/', wishlist_remove, name='wishlist_remove'),

    #####product pages###########
    path('/products/LivingRoom' , view_livingroom, name="livingroom"),
    path('/products/Bedroom' , view_bedroom, name="bedroom"),
    path('/products/diningroom' , view_diningroom, name="diningroom"),
    path('/products/studyroom' , view_studyroom, name="studyroom"),
    path('/products/kidsroom' , view_kidsroom, name="kidsroom"),
    path('/products/outdoor' , view_outdoor, name="outdoor"),
    path('/products/homedecor' , view_homedecor, name="homedecor"),
    path('/products/lamps&lightings' , view_lamps, name="lamps"),

    

]
