from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'user/profile.html', context)
