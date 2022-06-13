from django.urls import path,include
from api.views import OrderViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Order',OrderViewset)

urlpatterns = [
    path('', include(router.urls)),
]