from django.shortcuts import render

def barbershop(request):
    return render(request, 'barbershop/barbershop.html')
