from django.shortcuts import render
from . models import USERS_DATA


# Create your views here.

def create(request):
    if request.POST:
        Full_Name=request.POST.get('FullName')
        Email=request.POST.get('Email')
        Phone_No=request.POST.get('ContactNo')
        Description=request.POST.get('AboutProject')
        data=USERS_DATA(Full_Name=Full_Name,Email=Email,Contact_Number=Phone_No,About_Project=Description)
        data.save()
    return render(request,'index.html')


def view(request):
    info=USERS_DATA.objects.all()
    return render(request,"data.html",{"datas":info})