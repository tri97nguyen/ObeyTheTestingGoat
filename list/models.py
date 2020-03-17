from django.db import models

# Create your models here.


class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='I am default value')
    listy = models.ForeignKey(List, default='')
    pass

