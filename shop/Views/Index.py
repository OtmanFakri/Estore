from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers


from shop.models import Category, Customer, Product, Cart,Banner,Weekly_Deal,News
def index(request):
        categories = Category.objects.all()
        Banners = Banner.objects.all()
        trending_products = Product.objects.order_by('-id')[:6]
        Weekly_Deals = Weekly_Deal.objects.order_by('-id').first()
        News5 = News.objects.order_by('-id')[:6]






        context={
                'Banners' : Banners,
                'categories':categories,
                'trending_products' : trending_products,
                'Weekly_Deal':Weekly_Deals,
                'News':News5,
                'trending_categorys':prd(),
        }
        return render(request, 'Pages/index.html' , context)


def prd():
    categories = Category.objects.all()

    data = []

    for category in categories:
        products = Product.get_products_by_category(category.id)
        product_list = list(products.values())
        
        category_data = {
            'category_name': category.category_name,
            'category_list': product_list,
        }
        print(list(products.values()))
        
        data.append(category_data)



    return data

