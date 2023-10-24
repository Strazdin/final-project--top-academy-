from django.shortcuts import render
from .models import Appointment
from barbershop.models import Barbers, Price
from datetime import datetime, timedelta

def appointment(request):
    all_time = ['08:00', '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00', '15:00',
            '16:00', '17:00', '18:00', '19:00']
    
    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")
    max_day_value = yesterday + timedelta(days=7)
    max_day_value = max_day_value.strftime("%Y-%m-%d") 

    barber_names = Barbers.objects.all()
    price_list = Price.objects.all()
            
    if request.GET.get('date') is None:
        dict_obj = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'all_time': all_time,
            'barber_names': barber_names,
            'step_1': True,
            'step': 'Шаг 1'
            }
        
        return render(request, 'appointment/appointment.html', dict_obj)
    else:
        barber = request.GET.get('barber')
        
        appointments = Appointment.objects.filter(day=request.GET.get('date'), brbr_id=Barbers.objects.get(barber_name=barber).id).all()

        barber_name = Barbers.objects.get(barber_name=barber)

        for obj in appointments:
            all_time.remove(obj.time.strftime("%H:%M"))

        if not all_time:
            error_switch = True
            message = 'Парикмахер занят'
            
        else:
            error_switch = False
            message = 'Данный парикмахер свободен'

        dict_obj = {
            'min_day_value': min_day_value,
            'max_day_value': max_day_value,
            'all_time': all_time,
            'barber_names': barber_names,
            'barber': request.GET.get('barber'),
            'barber_name': barber_name,
            'price_list': price_list,
            'step_1': False,
            'step_2': True,
            'step': 'Шаг 2',
            'choised_day': request.GET.get('date'),
            'message': message,
            'error_switch': error_switch
            }
        
        return render(request, 'appointment/appointment.html', dict_obj)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        barber = request.POST['barber']
        service = request.POST['service']
        day = request.POST['date']
        time = request.POST['time']
        barber_id = request.POST['barber_id']

        element = Appointment(name = name,
                        phone = phone,
                        barber = barber,
                        service = service,
                        day = day,
                        time = time,
                        brbr_id = barber_id)
        element.save()
        return render(request, 'appointment/thanks.html', {name: name})
    else:
        return render(request, 'appointment/thanks.html')