from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class CourtDecision(models.Model):
    """
    Model description to be used in the app, it stores a single
    entry for the court decisions.
    """
    n_processo = models.CharField( max_length=30, validators=[MinLengthValidator(5)])
    ementa = models.CharField(max_length=5000)
    favor_contribuinte = models.CharField(max_length=1)
    id_cliente = models.IntegerField()

    def __str__(self):
        return self.n_processo