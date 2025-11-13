# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet,PengaduanViewSet
# from .views import WargaListAPIView, pengaduanListAPIView

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
#     path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
#     path('warga/<int:pk>/', WargaListAPIView.as_view(), name='api-warga-detail'),
#     path('pengaduan/',pengaduanListAPIView.as_view(), name='api-pengaduan-list'),
#     path('pengaduan/<int:pk>/',pengaduanListAPIView.as_view(), name='api-pengaduan-detail'),
# ]   