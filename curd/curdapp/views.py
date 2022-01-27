from django.shortcuts import render, redirect
from .models import UserDetails
from .forms import UserForm
from django.http import HttpResponseRedirect
# Create your views here.

def show(request):
    user = UserDetails.objects.all()
    return render(request,'curdapp/home.html',{'user':user})

def create(request):
    user = UserForm()
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            print('User details are stored')
            return redirect('/')
    return render(request,'curdapp/create.html',{'user':user})

def update(request,id):
    user = UserDetails.objects.get(id=id)
    if request.method == 'POST':
        user1 = UserForm(request.POST,instance=user)
        if user1.is_valid():
            user1.save()
            return HttpResponseRedirect('/')
    return render(request,'curdapp/update.html',{'user':user})

def delete(request,id):
    user = UserDetails.objects.get(id=id)
    user.delete()
    return redirect('/')