from django.urls import path

from .views import PlanejamentoList, PlanejamentoCreateView, PlanejamentoUpdateView, ItensPlanejados

urlpatterns = [
    path('<int:celula_id>/', PlanejamentoList.as_view(), name='list_planejamento'),
    path('<int:celula_id>/create/', PlanejamentoCreateView.as_view(), name='create_planejamento'),
    path('<int:celula_id>/edit/<int:pk>', PlanejamentoUpdateView.as_view(), name='edit_planejamento'),
    path('', ItensPlanejados.as_view(), name='itens_planejados'),
    path('pi/<int:pi_id>/', ItensPlanejados.as_view(), name='itens_planejados_get_pi'),
]