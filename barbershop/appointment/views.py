from django.shortcuts import render
from .models import Appointment
from barbershop.models import Barbers, Price
from user.models import Profile
from datetime import datetime, timedelta
from django.contrib import messages
import re

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
            'step_2': False,
            'step': 'Шаг 1'
            }
        
        return render(request, 'appointment/appointment.html', dict_obj)
    else:
        barber = request.GET.get('barber')
        date = request.GET.get('date')

        if barber and date:
            appointments = Appointment.objects.filter(day=request.GET.get('date'), barber_id=Barbers.objects.get(barber_name=barber).id).all()
            barber_name = Barbers.objects.get(barber_name=barber)
        else:
            messages.error(request, 'Выберите барбера и дату')
            return render(request, 'barbershop/barbershop.html')

        client = ''

        if request.user.is_authenticated == True:
            client = Profile.objects.get(username=request.user.username)

        for obj in appointments:
            all_time.remove(obj.time.strftime("%H:%M"))

        if not all_time:
            error_switch = True
            message = '(Занят)'
            
        else:
            error_switch = False
            message = ''

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
            'error_switch': error_switch,
            'client': client
            }
        
        return render(request, 'appointment/appointment.html', dict_obj)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        day = request.POST['date']
        time = request.POST['time']
        barber_id = request.POST['barber_id']
        user_id = request.POST['user_id']
        service = request.POST['service']
        if time and service:
            if phone.isdigit() and len(phone) == 10:
                if name.isalpha() and len(name) >= 2:
                    service_id = Price.objects.get(service = service).id
                    name = name.capitalize()

                    element = Appointment(name = name,
                                    phone = phone,
                                    day = day,
                                    time = time,
                                    barber_id = barber_id,
                                    service_id = service_id,
                                    client_id = user_id,
                                    )
                    
                    element.save()

                    count_appointments = Appointment.objects.filter(client_id=request.user.id).count()
                    message_discount = ''
                    
                    if count_appointments % 2 == 0:
                        message_discount = "Эта стрижка для вас бесплатна!"

                    dict_obj = {
                        'name': name,
                        'day': day,
                        'time': time,
                        'message_discount': message_discount
                        }
                    

                    return render(request, 'appointment/thanks.html', dict_obj)
                else:
                    messages.error(request, 'Имя должно состоять только из букв')
                    return render(request, 'barbershop/barbershop.html')
            else:
                messages.error(request, 'Номер телефона должен состоять из 10 цифр')
                return render(request, 'barbershop/barbershop.html')
        else:
            messages.error(request, 'Выберите время и стрижку')
            return render(request, 'barbershop/barbershop.html')
    else:
        # return render(request, 'appointment/thanks.html')
        pass