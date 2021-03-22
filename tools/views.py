from tools.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import ToolSerializer
from .models import Tool


class ToolListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ToolDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
