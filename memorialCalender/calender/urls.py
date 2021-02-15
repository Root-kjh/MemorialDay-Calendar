from django.urls import path

from . import views

urlpatterns = [
    path('set', views.SetCalender.as_view()),
    path('show', views.ShowCalender.as_view())
]