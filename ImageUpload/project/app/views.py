from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def UploadImage(request):
    if request.method=="POST":
        imagename=request.POST['iname']
        pics=request.FILES['image']

        newimg=Imagedata.objects.create(Imagename=imagename,Image=pics)
        return redirect('show')
    
def ImageFetch(request):
    all_img=Imagedata.objects.all()
    return render(request,"show.html",{'key1':all_img})

def Back(request):
    return render(request,"index.html")
