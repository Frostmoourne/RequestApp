from django.urls import path
from .views import *

app_name = "requests"

urlpatterns = [
    path('requests/', RequestApi.as_view()),
    path('requests/create', RequestCreateApi.as_view()),
    path('requests/<int:pk>', RequestUpdateApi.as_view()),
    path('requests/<int:pk>/delete', RequestDeleteApi.as_view()),
]
