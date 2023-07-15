from django.views import View
from django.shortcuts import render
from django.shortcuts import render, redirect

from shop.models import Category, Customer, Product, Cart,Banner,Weekly_Deal
def index(request):
        categories = Category.objects.all()
        Banners = Banner.objects.all()
        trending_products = Product.objects.order_by('-id')[:6]
        Weekly_Deals = Weekly_Deal.objects.order_by('-id').first()


        print(Weekly_Deals.product.price)

        context={
                'Banners' : Banners,
                'categories':categories,
                'trending_products' : trending_products,
                'Weekly_Deal':Weekly_Deals,
        }
        return render(request, 'Pages/index.html' , context)
