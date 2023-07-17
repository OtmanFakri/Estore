
from django.urls import path
from .Views import  Singup, Login ,Index , wishlist,Cart,Chechkount,News,product


handler404 = 'shop.Views.handler404.handler404'

urlpatterns = [
    path("", Index.index, name="ShopHome"),
    path("signup/", Singup.Signup.as_view(), name="SignUp"),
    path("login/", Login.Login.as_view(), name="LogIn"),
    
    path('wishlist/', wishlist.index, name='index_wishlist'),
    path('cart/', Cart.index, name='index_cart'),

    path('wishlist/add/<int:product_id>/', wishlist.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_id>/', wishlist.remove_from_wishlist, name='remove_from_wishlist'),

    path('cart/add/<int:product_id>/', Cart.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', Cart.remove_from_cart, name='remove_from_cart'),

    path('prodct/', Index.prd, name='my-view'),

    path('Checkout/', Chechkount.checkout, name='Checkout'),

    path('news/', News.index, name='index'),
    path('news/<int:news_id>/', News.one_news, name='one_news'),

    path('products/', product.all_products, name='all_products'),
    path('products/category/<int:category_id>/', product.products_by_category, name='products_by_category'),
    path('product/<int:product_id>/', product.product_detail, name='product_detail'),


    ]