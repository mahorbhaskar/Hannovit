from django.shortcuts import render, HttpResponseRedirect
from .forms import Employee
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.

#This Function Add and Show all The Entries
def add_show(request):
    if request.method == 'POST':
        fm = Employee(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            pn=fm.cleaned_data['pan']
            ag=fm.cleaned_data['age']
            gn=fm.cleaned_data['gender']
            el=fm.cleaned_data['email']
            ct=fm.cleaned_data['city']
            reg=User(name=nm,pan=pn,age=ag,gender=gn,email=el,city=ct)
            reg.save()
            fm=Employee()
    else:
        fm=Employee()
    emp = User.objects.all()
    return render(request,'enroll/addandshow.html', {'form':fm,'em':emp})
#This function will Update and Edit
def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=Employee(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=Employee(instance=pi)
    return render(request, 'enroll/update.html', {'form':fm})

#This function will Delete the Entries
def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')