from django.shortcuts import render, redirect
from datetime import datetime
from homepage.models import SignUp
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = {
        "file_name" : "m1.jpg"
    }
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def help(request):
    return render(request, 'help.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname") 
        lname = request.POST.get("lname") 
        state = request.POST.get("state") 
        city = request.POST.get("city") 
        pincode = request.POST.get("pincode") 
        password = request.POST.get("password") 
        phoneno = request.POST.get("phoneno") 
        region = request.POST.get("region") 
        join_date = datetime.today()
        signup = SignUp(region = region, fname = fname, lname = lname, city = city, pincode = pincode, state = state, phoneno = phoneno, password = password, join_date = join_date) 
        if signup.verifyFields():
            signup.save()   
            messages.success(request, "Account Succesfully Created") 
            return render(request, 'home.html')

        else:
            pass
    return render(request, 'signup.html')
            
    

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

