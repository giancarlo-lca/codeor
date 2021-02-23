from django.shortcuts import render
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from apps.celulas.models import Celula
from apps.pi.models import Pi
from .models import Planejamento
from .forms import PlanejamentoModelForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sistemacodeor.decorators import controle_acesso_pi_usuario
# Create your views here.

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@method_decorator(controle_acesso_pi_usuario, name='dispatch')
class PlanejamentoList(ListView):
    model = Planejamento
    # comentar depois para ficar o padrão celulas/celula_list.html
    template_name = 'planejamentos/planejamento_list.html'

    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('entrei aqui')
        celula = Celula.objects.get(id=self.kwargs['celula_id'])
        context['celula'] = celula

        return context

    def get_queryset(self):
        # print('entrei aqui')
        celula = Celula.objects.get(id=self.kwargs['celula_id'])
        return Planejamento.objects.filter(celula=celula)
        


# Create
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@method_decorator(controle_acesso_pi_usuario, name='dispatch')
class PlanejamentoCreateView(BSModalCreateView):
    template_name = 'planejamentos/planejamento_form.html'
    form_class = PlanejamentoModelForm
    success_message = 'Planejamento adicionado!'
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        celula_id = self.kwargs['celula_id']
        pi_id = self.kwargs['pi_id']
        
        return reverse_lazy('list_planejamento', kwargs={'pi_id': pi_id, 'celula_id': celula_id })      

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('criar planejamento')

        context['titulo_form'] = 'CRIAR'
        return context
    
    def form_valid(self, form):
        # """If the form is valid, save the associated model."""
        # print(self.kwargs)
        celula_id = self.kwargs['celula_id']
        celula = Celula.objects.get(id=celula_id)

        form.instance.celula = celula

        return super().form_valid(form)
    
    
# Update
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@method_decorator(controle_acesso_pi_usuario, name='dispatch')
class PlanejamentoUpdateView(BSModalUpdateView):
    model = Planejamento
    template_name = 'planejamentos/planejamento_form.html'
    form_class = PlanejamentoModelForm
    success_message = 'Planejamento alterado!'
    # success_url = reverse_lazy('index')
    
    def get_success_url(self):
        celula_id = self.kwargs['celula_id']
        pi_id = self.kwargs['pi_id']
        
        return reverse_lazy('list_planejamento', kwargs={'pi_id': pi_id, 'celula_id': celula_id })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('criar planejamento')

        context['titulo_form'] = 'ALTERAR'
        return context
    
    def form_valid(self, form):
        # """If the form is valid, save the associated model."""
        # print(self.kwargs)
        celula_id = self.kwargs['celula_id']
        celula = Celula.objects.get(id=celula_id)

        form.instance.celula = celula

        return super().form_valid(form)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
@method_decorator(controle_acesso_pi_usuario, name='dispatch')
class ItensPlanejados(ListView):
    model = Planejamento
    # comentar depois para ficar o padrão celulas/celula_list.html
    template_name = 'planejamentos/itens_planejados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
                
        if 'pi_id' in self.kwargs:
            
            pi = Pi.objects.get(id=self.kwargs['pi_id'])
            context['pi_descricao'] = pi.descricao
            context['pi_id'] = pi.id

        context['PI'] = Pi.objects.all().order_by('descricao')
        

        return context

    def get_queryset(self):
        
        if (self.request.user.is_staff and 'pi_id' not in self.kwargs):
            return Planejamento.objects.filter(id=0000)

        pi = 0

        if 'pi_id' in self.kwargs:
            pi = Pi.objects.get(id=self.kwargs['pi_id'])

        else:
            pi = self.request.user.funcionario.pi
        
        celulas = Celula.objects.filter(pi=pi)
        return Planejamento.objects.filter(celula__in=celulas)
