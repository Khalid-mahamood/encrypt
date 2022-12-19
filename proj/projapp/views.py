from django.shortcuts import render, redirect

from cryptography.fernet import Fernet
from .models import encrypt

def index(request):
    encrypts = encrypt.objects.all()
    return render(request,'index.html',{'encrypts':encrypts})

def tex(request):
    encrypts = encrypt.objects.all()
    if request.method == "POST":
        input_string = request.POST.get('Name')
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_string = fernet.encrypt(input_string.encode())
        text = encrypt(Name=input_string)
        text.save()
        return redirect('/')
    return render(request, "tex.html",{'encrypts':encrypts})
