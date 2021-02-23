from .models import Celula
from bootstrap_modal_forms.forms import BSModalModelForm


class CelulaModelForm(BSModalModelForm):
    class Meta:
        model = Celula
        fields = '__all__'
    