from django.shortcuts import render
from .models import Barbers

def barbershop(request):
    barbers = Barbers.objects.all()
    return render(request, 'barbershop/barbershop.html', {'barbers': barbers})
