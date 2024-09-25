from django.db import models

# Create your models here.

class Expense(models.Model):
    name =models.CharField(max_length=100)
    amount =models.DecimalField( max_digits=5, decimal_places=2)
    category= models.CharField(max_length=50)
    date =models.DateField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

