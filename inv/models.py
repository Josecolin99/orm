from django.db import models
from app1.models import ModeloAuditoria
from django.db.models import Q


# Create your models here.

class Question(ModeloAuditoria):
    question_text = models.CharField(max_length=50)
    

class Choice(ModeloAuditoria):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
#Se especifica de donde se quiere tomar la migracion

#Se espeficia a que bd se hace la migracion
#py manage.py migrate inv --database db_inv

