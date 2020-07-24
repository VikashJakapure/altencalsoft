from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from . models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'book/index.html')

class BookList(ListView):
    queryset = Book.objects.all().order_by("name")
    template_name = "book/index.html"
    context_object_name = 'bookslist'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/details.html'
    context_object_name = 'book'



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
