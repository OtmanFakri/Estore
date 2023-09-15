from django.shortcuts import render
from ..models import Product,Category,Review,Cart,Wishlist,Customer
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404


def all_products(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categori = Category.objects.order_by('-id')[:5]

    return render(request, 'Pages/shop-left-sidebar.html', {'page_obj': page_obj, 'categoris': categori})

def products_by_category(request, category_id):
    products = Product.get_products_by_category(category_id)

    paginator = Paginator(products, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categori=Category.objects.order_by('-id')[:5]

    return render(request, 'Pages/shop-left-sidebar.html', 
                  {'page_obj': page_obj,
                   'categoris':categori})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product_id)
    products_categorys = Product.get_products_by_category(product.category.id)[:6]


    return render(request, 'Pages/single-product.html', {
        'product': product,
        'reviews':reviews,
        'products_categorys':products_categorys})

