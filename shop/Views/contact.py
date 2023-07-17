from django.shortcuts import render

def contact(request):
    
    return render(request, 'Pages/contact.html')