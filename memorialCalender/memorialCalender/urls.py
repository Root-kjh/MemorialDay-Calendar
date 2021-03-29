from django.urls import path, include
from rest_framework_nested import routers
from calender.views import CalenderViewSet
from user.views import UserViewSet
from auth.views import SigninViewSet, SignupViewSet

router = routers.SimpleRouter()
router.register(r'auth/signup', SignupViewSet, 'Auth')
router.register(r'auth/signin', SigninViewSet, 'Auth')
router.register(r'user', UserViewSet)
calender_router = routers.NestedSimpleRouter(router, r'user', lookup="user")
calender_router.register(r'calender', CalenderViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(calender_router.urls)),  
]