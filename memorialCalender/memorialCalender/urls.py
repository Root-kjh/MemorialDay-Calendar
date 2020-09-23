from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('calender/',include('calender.urls'))
]