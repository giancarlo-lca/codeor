from .models import Planejamento
from bootstrap_modal_forms.forms import BSModalModelForm


class PlanejamentoModelForm(BSModalModelForm):
    class Meta:
        model = Planejamento
        fields = ('valor', 'status', 'item')
