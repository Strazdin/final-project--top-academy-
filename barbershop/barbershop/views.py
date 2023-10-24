from django.shortcuts import render
from .models import Barbers, Price, Portfolio

def barbershop(request):
    barbers = Barbers.objects.all()
    price_list = Price.objects.all()
    portfolio = Portfolio.objects.all()

    dict_obj = {
        'barbers': barbers,
        'price_list': price_list,
        'portfolio': portfolio
    }

    return render(request, 'barbershop/barbershop.html', dict_obj)
