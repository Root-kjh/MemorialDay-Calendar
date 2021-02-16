from django.urls import path

from . import views

urlpatterns = [
    path('set/', views.SetCalender.as_view()),
    path('show/', views.ShowCalender.as_view()),
    path('del/<int:id>/', views.DeleteCalender.as_view()),
    path('update/<int:id>/', views.UpdateCalender.as_view())
]