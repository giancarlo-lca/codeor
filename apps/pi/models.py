from django.db import models

# Create your models here.

class Base(models.Model):
    codigo = models.CharField(unique=True, max_length=20, null=False)
    descricao = models.CharField(max_length=150, null=False)

    class Meta:
        abstract = True

class Pi(Base):
    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'pi'

    def find_and_save(self, codigo, descricao):
        try:
            #print(codigo)
            obj = __class__.objects.get(codigo=codigo)
            return obj
        except:
            self.codigo = codigo
            self.descricao = descricao
            self.save()
            return self

