from django.urls import path

from . import views

urlpatterns = [
    path('show', views.ShowCalender.as_view())
]