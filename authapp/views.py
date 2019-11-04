from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import http
from .models import Register
from .forms import LoginForm
from .forms import RegForm
import random
import http.client
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail

# Create your views here.

def register(request):
    if request.method=='POST':
        reg= RegForm(request.POST)

        if reg.is_valid():
            
            x=otp_send(request)

            if x:
                return render(request,'homeapp/otp_input.html')
            else:
                return render(request,'authapp/signup.html')
               
        else:
            
            return render(request,'authapp/signup.html')
    else:
        return render(request, 'authapp/signup.html')


def otpvalidation(request):
    newotp=request.POST['otp']
    oldotp=request.POST['otp']
    if newotp==oldotp:
        form=RegForm(request.session['details'])
        new_user=User.objects.create_user(username=request.session["uname"],password=request.session['pwd'])
        new_user.save()
        form.save()        
        login(request)
        return render(request,'homeapp/price.html')
    else:
        return render(request,'authapp/otp_input.html')


def otp_send(request):
    ot = str(random.randint(100000, 999999))
    phno=request.POST["phno"]
    request.session["uname"]=request.POST["uname"]
    request.session["pwd"] = request.POST["pwd"]
    # subject="registation otp"
    request.session["details"]=request.POST
    request.session["otp"]=ot
    conn=http.client.HTTPConnection("api.msg91.com")
    payload = "{\"sender\":\"VARUNK\", \"route\": \"4\", \"country\": \"91\", \"sms\": [{\"message\":\"" + ot + "\", \"to\": [\"" + phno + "\"]}]}"
    headers={'authkey':"301145AUnx4zFX7wp5db6e535",
             'content-type':"application/json"}
    conn.request("POST","/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&aferminute=&response=&campaign=",payload,headers)
    data=conn.getresponse()
    print('otp_send sucess')
    res = json.loads(data.read().decode("UTF-8"))
    print('res sucess')
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False

# @login_required
def login(request):
    if request.method == 'POST':
         uname = request.POST['uname']
         pwd = request.POST['pwd']
         user = authenticate(username=uname, password=pwd)
         if user is not None: 
                #  send_useremail(request)            
                 return HttpResponse('sucess')
                 
         else:
             return HttpResponse('not sucess')
    else:
        return render(request, 'authapp/signin.html')
    #   return render(request,'homeapp/price.html')

def my_logout(request):
    logout(request)
    return render(request,'homeapp/index.html')

# def send_useremail(request):
#     send_mail('Welcome to our Shop', 
#     'this is a welcome message','varunandpython@gmail.com',
#     ['90.varunkrishna@gmail.com'],fail_silently=False)
