from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers  import Serializer
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from . serializers import *
from . models import *
from django.shortcuts import render,redirect
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            # login(request,user)
            return render(request,'dashboard.html')

        else:
            messages.error(request,"you have not loggd in")
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('logout')

def dashboard(request):
    return render(request,'dashboard.html')

def manage_customer(request):
    selectdata = Customer.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_customer.html',context)

def delete_customer(request,id):
    selectdata = Customer.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_customer')


def new_customer(request):
    selectdata = Customer.objects.all()
    if request.method == "POST":
        post = Customer()
        post.address = request.POST['address']
        post.names = request.POST['names']
        post.email = request.POST['email']
        post.gender = request.POST['gender']
        post.phonenumber = request.POST['phonenumber']
        post.National_id  = request.POST['national_id']
        post.save()
    return render(request,'new_customer.html',{"data":selectdata})

def edit_customer(request,id):
    selectone = Customer.objects.get(id=id)
    if  request.method == 'POST':
        selectone.address = request.POST['address']
        selectone.names = request.POST['names']
        selectone.gender = request.POST['gender']
        selectone.phonenumber = request.POST['phonenumber']
        selectone.National_id = request.POST['natioal_id']
        selectone.save()
    return render(request,'edit_customer.html',{"data":selectone})

################ detial of the customer ###################

def manage_herbal(request):
    selectdata = Herbals.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_herbal.html',context)

def delete_herbal(request,id):
    selectdata = Herbals.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_herbal')

def add_herbal(request):
    if request.method == 'POST':
        post = Herbals()
        post.image = request.FILES['image']
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.video = request.FILES['video']
        post.save()
    return render(request,'add_herbal.html')

################ imigani ###########################

def add_imigani(request):
    if request.method == "POST":
        post = Imigani()
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.save()
    return render(request,'add_imigani.html')

def manage_imigani(request):
    selectdata = Imigani.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_imigani.html',context)

def delete_imigani(request,id):
    selectdata = Imigani.objects.get(id=id)
    selectdata.delete()
    return redirect('manage_imigani')


def add_amateka(request):
    selectdata = Amateka.objects.all()
    if request.method == "POST":
        post = Amateka()
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.image = request.FILES['image']
        post.save()
    return render(request,'add_amateka.html',{"data":selectdata})

def manage_amateka(request):
    selectdata = Amateka.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_amateka.html',context)

def delete_amateka(request,id):
    selectdata = Amateka.objects.get(id=id)
    selectdata.delete()
    return redirect('delete_amateka')


######## DIY ##########

def add_diy(request):
    selectdata = Diy.objects.all()
    if request.method == "POST":
        post = Diy()
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.video = request.FILES['image']
        post.save()
    return render(request,'add_diy.html',{"data":selectdata})

def manage_diy(request):
    selectdata = Diy.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_diy.html',context)

def delete_diy(request,id):
    selectdata = Diy.objects.get(id=id)
    selectdata.delete()
    return redirect('delete_diy')


########### sakwe ##########


def add_sakwe(request):
    selectdata = Sakwe.objects.all()
    if request.method == "POST":
        post = Sakwe()
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.answer = request.POST['answer']
        post.save()
    return render(request,'add_sakwe.html',{"data":selectdata})

def manage_sakwe(request):
    selectdata = Sakwe.objects.all()
    context = {
        "data":selectdata
    }
    return render(request,'manage_sakwe.html',context)

def delete_sakwe(request,id):
    selectdata = Sakwe.objects.get(id=id)
    selectdata.delete()
    return redirect('delete_sakwe')
