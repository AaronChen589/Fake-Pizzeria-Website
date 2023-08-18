from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Page that shows all pizzas
    path('pizzas/', views.pizzas, name="pizzas"),

    # Show Toppings for Specific pizza
    path('pizzas/<int:pizza_id>/toppings/', views.toppings, name='toppings'),

]


