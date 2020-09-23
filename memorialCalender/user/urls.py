from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('password-modify', views.password_modify, name='password_modify'),
    path('logout', views.logout, name='logout'),
    path('withdraw', views.withdraw, name='withdraw')
]