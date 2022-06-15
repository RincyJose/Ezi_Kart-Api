from django.urls import path,include
from api.views import OrderViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Order',OrderViewset)
# router.register('List',UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]