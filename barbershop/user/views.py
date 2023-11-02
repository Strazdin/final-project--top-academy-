from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'user/profile.html', context)

def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    context = {'profile': prof}
    return render(request, 'user/profile.html', context)
