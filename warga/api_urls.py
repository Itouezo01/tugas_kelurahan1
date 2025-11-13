# warga/api_urls.py
from django.urls import path
from .views import WargaListAPIView, pengaduanListAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaListAPIView.as_view(), name='api-warga-detail'),
    path('pengaduan/',pengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    path('pengaduan/<int:pk>/',pengaduanListAPIView.as_view(), name='api-pengaduan-detail'),
]   