from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calender.views import CalenderViewSet
from user.views import UserViewSet
from auth.views import SigninViewSet, SignupViewSet
router = DefaultRouter()
router.register(r'calender', CalenderViewSet)
router.register(r'user', UserViewSet)
router.register(r'auth/signup', SignupViewSet, 'Auth')
router.register(r'auth/signin', SigninViewSet, 'Auth')
urlpatterns = router.urls