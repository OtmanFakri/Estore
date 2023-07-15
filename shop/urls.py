
from django.urls import path
from .Views import  Singup, Login ,Index
urlpatterns = [
    path("", Index.index, name="ShopHome"),
    path("signup/", Singup.Signup.as_view(), name="SignUp"),
    path("login/", Login.Login.as_view(), name="LogIn"),
    ]