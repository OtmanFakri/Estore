from django.shortcuts import render
from ..models import Product,Category
from django.shortcuts import render, get_object_or_404


def all_products(request):
    products = Product.objects.all()
    categori=Category.objects.order_by('-id')[:5]
    return render(request, 'Pages/shop-left-sidebar.html', 
                  {'products': products,
                   'categoris':categori})

def products_by_category(request, category_id):
    products = Product.get_products_by_category(category_id)
    categori=Category.objects.order_by('-id')[:5]

    return render(request, 'Pages/shop-left-sidebar.html', 
                  {'products': products,
                   'categoris':categori})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'Pages/single-product.html', {'product': product})