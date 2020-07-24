

from django.urls import path
from . views import BookList,BookDetailView
from django.contrib.auth import  views as auth_views
from book import views
app_name = 'book_app'

urlpatterns = [
    path("", BookList.as_view(),name="list"),
    path("<int:pk>",BookDetailView.as_view(),name="details"),
    path('sign_up/', views.sign_up, name="sign-up"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),


]