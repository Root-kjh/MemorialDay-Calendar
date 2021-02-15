from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from memorialCalender import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
router.register(r'', views.CalenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('user/', include('user.urls')),
    path('calender/', include('calender.urls'))
]