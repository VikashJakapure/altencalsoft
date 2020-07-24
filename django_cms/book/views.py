from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from book.forms import BookForm
from book.models import *
@login_required
def index(request):
    return render(request,'book/index.html')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'book/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

class Bookview(View):
    def get(self,request):
        obj =Book.objects.all()
        return render(request,'book/show.html',{'obj':obj})
class AddbookView(View):
    def get(self,request):
        obj=BookForm()
        return render(request,'book/add.html',{'obj':obj})

    def post(self,request):
        obj=BookForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/book/show/')