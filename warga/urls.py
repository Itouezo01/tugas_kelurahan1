from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    PengaduanListView,
    WargaCreateView,
    PengaduanCreateView,  
    WargaUpdateView, 
    WargaDeleteView,
    PengaduanUpdateView,
    PengaduanDeleteView,    #tambah
)

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),  
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'), 

    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), 
    
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),    
    
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan_edit'),
    path('pengaduan/<int:pk>/delete/', PengaduanDeleteView.as_view(), name='pengaduan_delete'),   #tambah
]
