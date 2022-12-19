from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Data
from django.db.models import Q

def isValidInt(input):
    return not input.isdigit()
@login_required(login_url='login')
def HomePage(request):
   return render(request,"home.html")

def Signup(request):
   if request.method=='POST':
        id=request.POST.get('id')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        elif len(id)!=16 |  (isValidInt(id)) :
             return HttpResponse("Your ID is invalid")
 
        else:

            my_user=User.objects.create_user(id,email,pass1)
            my_user.save()
            return redirect('login')
        



   return render (request,'signup.html')

def Login(request):

  if request.method=='POST':
        id=request.POST.get('id')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=id,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("id or Password is incorrect!!!")




  return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')  

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        data = Data.objects.filter(multiple_q)
    else:
        data = Data.objects.all()
     
    return render(request, 'home.html',{"data":data})    
