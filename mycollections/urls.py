from django.urls import path
from . import views


app_name = 'mycollections'

urlpatterns = [
	path('', views.HomepageView.as_view(), name='homepage'),
	path('collection/<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('collection/create/', views.CollectionCreate.as_view(), name='collection_create'),
    path('aplicacoes/<aplicacao_proprietario_slug>/<aplicacao_slug>/<propriedade_slug>/clientes/novo/', views.ClienteCreate.as_view(), name='cliente_create'),
    path('aplicacoes/<aplicacao_proprietario_slug>/<aplicacao_slug>/<propriedade_slug>/clientes/info/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('aplicacoes/<aplicacao_proprietario_slug>/<aplicacao_slug>/<propriedade_slug>/clientes/editar/<int:pk>/', views.ClienteUpdate.as_view(), name='cliente_update'),
    #path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('collection/update/<int:pk>/', views.CollectionUpdate.as_view(), name='collection_update'),
    path('collection/delete/<int:pk>/', views.CollectionDelete.as_view(), name='collection_delete'),
    path('aplicacoes/<aplicacao_proprietario_slug>/<aplicacao_slug>/<propriedade_slug>/clientes/excluir/<int:pk>/', views.ClienteDelete.as_view(), name='cliente_delete'),
	]
