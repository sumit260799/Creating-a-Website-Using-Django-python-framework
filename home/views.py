from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    return render(request, "index.html")
def about(request): 
    return render(request, "about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name,email = email,phone = phone,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
     
        
    

    return render(request, "contact.html")
def services(request):
    return render(request, "services.html")