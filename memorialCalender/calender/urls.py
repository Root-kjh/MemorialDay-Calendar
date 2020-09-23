from django.urls import path

from . import views

urlpatterns = [
    path('show', views.show_calender, name='show_calender'),
    path('set', views.set_calender, name='set_calender')
]