
from book import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('show/', views.Bookview.as_view()),
    path('add/',views.AddbookView.as_view()),

]