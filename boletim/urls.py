from django.urls import path
from . import views

urlpatterns = [
    path('boletim/list/', views.BoletimListView.as_view(), name='boletim_list'),
#     path('gcm/create/', views.GcmCreateView.as_view(), name='gcm_create'),
path('boletim/<int:pk>/detail/', views.BoletimDetailView.as_view(), name='boletim_detail'),
#     path('gcm/<int:pk>/update/', views.GcmUpdateView.as_view(), name='gcm_update'),
    path('boletim/<int:pk>/delete/', views.BoletimDeleteView.as_view(), name='boletim_delete'),
]