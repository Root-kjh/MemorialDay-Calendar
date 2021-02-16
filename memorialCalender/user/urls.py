from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view()),
    path('signin/', views.Signin.as_view()),
    path('password_modify/', views.PasswordModify.as_view()),
    path('withdraw/', views.Withdraw.as_view())
]