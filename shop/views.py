from django.shortcuts import render, HttpResponse
from datetime import datetime
from shop.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):

    context = {
        'var1': 'value 1',
        'var2': 'value 2'
    }

    return render(request, 'index.html', context)
    # return HttpResponse('This is homepage')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        contact = Contact(
            name = name,
            email = email,
            phone = phone,
            message = message,
            date = datetime.today()
        )
        contact.save()
        messages.success(request, 'Form submitted successfully.')

    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')
