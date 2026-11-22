from django.urls import path
from . import views

urlpatterns = [
    path('gcm/list/', views.GcmListView.as_view(), name='gcm_list'),
    path('gcm/create/', views.GcmCreateView.as_view(), name='gcm_create'),
    path('gcm/<int:pk>/detail/', views.GcmDetailView.as_view(), name='gcm_detail'),
    path('gcm/<int:pk>/update/', views.GcmUpdateView.as_view(), name='gcm_update'),
    path('gcm/<int:pk>/delete/', views.GcmDeleteView.as_view(), name='gcm_delete'),
]