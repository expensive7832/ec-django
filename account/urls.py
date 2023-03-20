from django.urls import path
from .views import Signup, Login

urlpatterns =[
    path("signup/", Signup, name="signup"),
    path("login/", Login, name="login"),
]




