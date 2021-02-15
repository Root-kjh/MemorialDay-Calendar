from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view()),
    path('signin/', views.Signin.as_view()),
]