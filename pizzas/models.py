from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
   

class Topping(models.Model):

    text = models.CharField(max_length=50)
    pizza_type = models.ForeignKey(Pizza, on_delete=models.CASCADE, default="cheese", related_name='toppings')

    def __str__(self):
        return self.text
        
    

