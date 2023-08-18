from django.shortcuts import render
from .models import Pizza, Topping


# Create your views here.
def index(request):
    """Homepage for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def toppings(request, pizza_id):
    """ show a pizza and all it's toppings"""
    # toppings = Topping.objects.get(id=pizza_id)
    # context = {'toppings':toppings}
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings.all()
    context = {'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)
