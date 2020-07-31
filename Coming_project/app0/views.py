from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import item,category
from django.urls import reverse
from .forms import createForm
from django.contrib import auth
import os


def main(request):
    Item = item.objects.all()
    return render(request,'main.html',{"main_key":Item})

def detail(request,detail_id):
    Item_detail = get_object_or_404(item, pk=detail_id)
    return render(request,'detail.html',{"detail_key":Item_detail})


def newitem(request):
    form = createForm()
    if request.method == "POST":
        new_val = item()
        new_val.img = request.FILES['img']
        new_val.name = request.POST.get('name',False)
        new_val.amount = request.POST.get('amount',False)
        new_val.date = request.POST.get('date',False)
        new_val.exp = request.POST.get('exp',False)
        new_val.plc = request.POST.get('where',None)
        place_id = category.objects.get(item ='where')
        new_val.plc = request.POST.get(place_id,False)
        new_val.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'newitem.html',{'form':form})

def newcate(request):
    cate = category.objects
    return render(request, 'newcate.html',{'cate':cate})


def home(request):
    return render(request,'home.html')

def loginhome(request):
    return render(request,'loginhome.html')

def signuphome(request):
    return render(request,'signuphome.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            errormasg ="잘못입력하셨습니다"
            return render(request, 'loginhome.html',{'errormasg':errormasg})
    else:
        return redirect('loginhome.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signuphome.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


