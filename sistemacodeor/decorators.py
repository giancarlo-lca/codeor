from django.http import HttpResponse
from django.shortcuts import redirect

from django.core.exceptions import PermissionDenied

def controle_acesso_pi_usuario(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        
        pi_id_usuario = request.user.funcionario.pi.id
        
        if 'pi_id' in kwargs:
            pi_id = kwargs['pi_id']

            if pi_id == pi_id_usuario:
                return view_func(request, *args, **kwargs)
            else:
                # ou raise PermissionDenied
                return HttpResponse('Você não tem autorização para esta página.')

        return view_func(request, *args, **kwargs)
    return wrapper_func