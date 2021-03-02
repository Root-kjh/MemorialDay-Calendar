from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalenderView.as_view()),
    path('/<int:id>', views.CalenderView.as_view())
]