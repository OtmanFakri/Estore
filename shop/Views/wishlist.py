
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Wishlist,Product
from django.shortcuts import render
from django.contrib import messages


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    #messages.success(request, 'Product added to wishlist!')
    return redirect('index_wishlist')


@login_required
def remove_from_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id, user=request.user)
    wishlist.delete()
    messages.success(request, 'Product removed from wishlist!')
    return redirect('index_wishlist')


@login_required
def index(request):
   
    Wishlists=Wishlist.objects.all()

    context={
                'Wishlists' : Wishlists,
              
        }

    #messages.success(request, 'Product added to wishlist!')
    return render(request,'Pages/wishlist.html',context)