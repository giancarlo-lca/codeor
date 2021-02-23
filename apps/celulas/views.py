#import io
from django.db.models import Q

from django.views import generic
from .forms import CelulaModelForm
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from django.views.generic.detail import SingleObjectMixin

from django.views.generic.base import View, TemplateView
#from reportlab.pdfgen import canvas
#from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
#import xhtml2pdf.pisa as pisa

from django.core.paginator import Paginator

from .models import Celula

from apps.pi.models import Pi

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sistemacodeor.decorators import controle_acesso_pi_usuario

# Create your views here.
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CelulasList(ListView):
    model = Celula
    # comentar depois para ficar o padrão celulas/celula_list.html
    template_name = 'celulas/celula_list.html'

    # paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if (self.request.user.is_staff):
            # print('olá1')
            context['pi_id'] = 0
            context['pi_descricao'] = ""
            context['PI'] = Pi.objects.all().order_by('descricao')
            
            # print(self.request.GET.get('select_pi_id'))
        return context

    def get_queryset(self):
        if (self.request.user.is_staff):
            return Celula.objects.filter(id=0000)

        
        pi_usuario = self.request.user.funcionario.pi
        return Celula.objects.filter(Q(dotacao__gt=0) | 
                                     Q(credito__gt=0) | 
                                     Q(despesasEmp__gt=0) | 
                                     Q(despesasPagas__gt=0), 
                                     pi=pi_usuario)
                                    #  .order_by('natureza__descricao')


@login_required(login_url='/accounts/login/')
@controle_acesso_pi_usuario
def celulaGetlist(request, pi_id):

    pi = Pi.objects.get(id=pi_id)
    listaCelulas = Celula.objects.filter(Q(dotacao__gt=0) | 
                                         Q(credito__gt=0) | 
                                         Q(despesasEmp__gt=0) | 
                                         Q(despesasPagas__gt=0), 
                                         pi=pi)
        
    context = {}
    context['pi_descricao'] = pi.descricao
    context['pi_id'] = pi.id
    context['PI'] = Pi.objects.all().order_by('descricao')
    context['object_list'] = listaCelulas
    # context['page_obj'] = page_obj
      # comentar depois para ficar o padrão celulas/celula_list.html   
    return render(request, 'celulas/celula_list.html', context)       
 
# Update
# @method_decorator(controle_acesso_pi_usuario, name='dispatch')
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CelulaUpdateView(BSModalUpdateView):
    model = Celula
    # template_name = 'examples/update_book.html'
    form_class = CelulaModelForm
    success_message = 'Celula alterada!'


    def get_success_url(self):
        if (self.request.user.is_staff):
            celula_id = self.kwargs['pk']
            celula = Celula.objects.get(id=celula_id)
            return reverse_lazy('list_celulas_get', kwargs={'pi_id': celula.pi.id})      
        else:
            return reverse_lazy('list_celulas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['celula'] = Celula.objects.get(id=self.kwargs['pk'])
        return context
       