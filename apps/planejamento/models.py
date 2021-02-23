from django.db import models
from django.shortcuts import reverse

from apps.celulas.models import Celula

# Create your models here.

class Planejamento(models.Model):
    STATUS_CHOICES = [
        ('PLANEJADO', 'Planejado'),
        ('EMPENHADO', 'Empenhado'),
        ('PAGO', 'Pago'),
        ('CANCELADO', 'Cancelado'),
        ('PENDENTE', 'Pendente'),

    ]
    item = models.TextField(max_length=200, null=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=False)

    celula = models.ForeignKey(Celula, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'planejamentos'

    # def get_absolute_url(self):
    #     return reverse('create_planejamento', args=[self.celula.pi.id, self.celula_id])
    
    # def save(self, *args, **kwargs):
    #     print(self.kwargs)
    #     ceulula = Celula.objects.get(id=self.kwargs['id_celula'])
    #     self.celula = celula
    #     super(Planejamento, self).save(*args, **kwargs)
    