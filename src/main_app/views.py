from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def home(request):
    time_now = timezone.localtime(timezone.now()) + timedelta(hours=6)
    context = {
        'time_now': time_now
    }
    return render(request, 'main_app/home.html', context)
