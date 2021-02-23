from django.urls import path

from .views import CelulasList, celulaGetlist, CelulaUpdateView

urlpatterns = [
    path('', CelulasList.as_view(), name='list_celulas'),
    path('<int:pi_id>/', celulaGetlist, name='list_celulas_get'),
    path('edit/<int:pk>', CelulaUpdateView.as_view(), name='edit_celula'),
]

