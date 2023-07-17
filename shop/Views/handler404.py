from django.shortcuts import render
from django.views.defaults import page_not_found, server_error

def handler404(request, exception):
    context = {}
    response = render(request, "errors/404.html", context=context)
    response.status_code = 404
    return response

def handler500(request):
    return render(request, 'errors/404.html', status=500)