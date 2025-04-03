from django.shortcuts import render
from .models import Lead

def home(request):
    if request.method == 'POST':
        # Создаем новую заявку
        Lead.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            service=request.POST.get('service')
        )
        return render(request, 'index.html', {'success': True})
    
    return render(request, 'index.html')