from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('urun-detay/<str:pk>', detail, name='detail'),
    path('sepetim/', cards, name='cards')
]