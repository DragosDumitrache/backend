from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
