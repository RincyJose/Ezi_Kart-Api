from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer
# Create your views here.


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']