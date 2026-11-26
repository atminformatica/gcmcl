from django.urls import path
from . import views

urlpatterns = [
    path('boletim/list/', views.BoletimListView.as_view(), name='boletim_list'),
    path('gcm/create/', views.BoletimIniciarView.as_view(), name='boletim_create'),
    path('boletim/<int:pk>/detail/', views.BoletimDetailView.as_view(), name='boletim_detail'),
    path('gcm/<int:pk>/update/', views.BoletimUpdateView.as_view(), name='boletim_update'),
    path('boletim/<int:pk>/delete/', views.BoletimDeleteView.as_view(), name='boletim_delete'),
    path('boletim/cancelar/', views.BoletimCancelarView.as_view(), name='boletim_cancelar'),
]