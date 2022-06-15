from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
# Create your views here.


class OrderViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    