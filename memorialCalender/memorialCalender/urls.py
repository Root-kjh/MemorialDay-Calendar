from django.urls import path, include

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('auth/, include(''))
    path('user', include('user.urls')),
    path('calender', include('calender.urls'))
]