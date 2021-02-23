from django.db import models

from apps.pi.models import Base

# Create your models here.

class AcaoGoverno(Base):
    def __str__(self):
        return self.codigo
    
    class Meta:
        db_table = 'acao_governo'

    def find_and_save(self, codigo, descricao):
        try:
            #print(codigo)
            obj = __class__.objects.get(codigo=codigo)
            #print(obj)
            return obj
        except:
            self.codigo = codigo
            self.descricao = descricao
            self.save()
            return self