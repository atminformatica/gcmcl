from django.urls import path
from . import views

urlpatterns = [
    path('boletim/list/', views.BoletimListView.as_view(), name='boletim_list'),
    path('boletim/create/', views.BoletimIniciarView.as_view(), name='boletim_create'),
    path('boletim/<int:pk>/detail/', views.BoletimDetailView.as_view(), name='boletim_detail'),
    path('boletim/<int:pk>/update/', views.BoletimUpdateView.as_view(), name='boletim_update'),
    path('boletim/<int:pk>/delete/', views.BoletimDeleteView.as_view(), name='boletim_delete'),
    path('boletim/<int:pk>/cancelar/', views.BoletimCancelarView.as_view(), name='boletim_cancelar'),

    path('<int:pk>/guarnicao/modal/', views.BoletimGuarnicaoModalView.as_view(), name='boletim_guarnicao_modal'),
    path('<int:pk>/guarnicao/adicionar/<int:gcm_id>/', views.BoletimGuarnicaoAdicionarView.as_view(), name='boletim_guarnicao_adicionar'),
    path('<int:pk>/guarnicao/remover/<int:gcm_id>/', views.BoletimGuarnicaoRemoverView.as_view(), name='boletim_guarnicao_remover'),

]