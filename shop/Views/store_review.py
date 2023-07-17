from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..models import Review, Customer

def store_review(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    customer, created = Customer.objects.get_or_create(user_id=current_user.id)

    if request.method == "POST":
        subject = request.POST.get('subject')
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        product_review = Review(
            product_id=prid,
            customer_id=customer.id,
            subject=subject,
            review=review,
            rating=rating,
        )
        product_review.save()

        messages.success(request, "Review Posted")
        return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
