

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Cart,Product
from django.shortcuts import render
from django.contrib import messages


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the existing cart item or create a new one
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        
        # Increase the quantity by 1 for an existing cart item or set it to 1 for a new item
        cart_item.qty += 1
        cart_item.save()
        
        # Redirect to the cart page or a relevant page
        return redirect('index_cart')
    else:
        # Handle the case where the user is not authenticated, e.g., redirect to a login page
        return redirect('LogIn')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    
    # Check if the cart item belongs to the current user
    if cart_item.user == request.user:
        cart_item.delete()
        
        # Redirect to the cart page or a relevant page
        return redirect('index_cart')
    else:
        # Handle the case where the cart item does not belong to the current user
        # Redirect to an error page or display an error message
        return redirect('index_cart')

@login_required
def index(request):
   
    Carts=Cart.objects.all()

    context={
                'Carts' : Carts,
              
        }

    #messages.success(request, 'Product added to wishlist!')
    return render(request,'Pages/cart.html',context)