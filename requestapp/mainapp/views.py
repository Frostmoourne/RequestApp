from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from .serializers import RequestReadSerializer, RequestUpdateSerializer
from .models import Request


class RequestCreateApi(generics.CreateAPIView):
    queryset = Request.objects.select_related()
    serializer_class = RequestUpdateSerializer


class RequestApi(generics.ListAPIView):
    queryset = Request.objects.select_related()
    serializer_class = RequestReadSerializer

    @method_decorator(cache_page(300))
    def dispatch(self, *args, **kwargs):
        return super(RequestApi, self).dispatch(*args, **kwargs)


class RequestUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Request.objects.select_related()
    serializer_class = RequestUpdateSerializer


class RequestDeleteApi(generics.DestroyAPIView):
    queryset = Request.objects.select_related()
    serializer_class = RequestReadSerializer
