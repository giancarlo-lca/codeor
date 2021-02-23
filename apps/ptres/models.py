from django.db import models

# Create your models here.

class Ptres(models.Model):
    codigo = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'ptres'

    def find_and_save(self, codigo):
        try:
            #print(cod)
            obj = __class__.objects.get(codigo=codigo)
            return obj
        except:
            self.codigo = codigo
            #self.description = desc
            self.save()
            return self

