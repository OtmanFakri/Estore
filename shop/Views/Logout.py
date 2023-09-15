from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy

class LogoutView(View):
    def get(self, request):
        # Log the user out
        logout(request)
        # Redirect to a success page or any other page you want
        return redirect(reverse_lazy('LogIn')) 