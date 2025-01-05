from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})

def create_blog(request):
    if request.method == "POST":
        form=Blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= Blog_form()
    return render(request,'view_form.html',{'form':form})

def delete_blog(request,id):
    did=get_object_or_404(Blog,pk=id)
    did.delete()
    return redirect('/')

def update_blog(request,id):
    if request.method == "POST":
        uid=get_object_or_404(Blog,pk=id)
        form=Blog_form(request.POST,request.FILES,instance=uid)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        uid=get_object_or_404(Blog,pk=id)
        form=Blog_form(instance=uid)
    return render(request,'view_form.html',{'form':form})

 