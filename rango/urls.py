from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),    #空字符串定位到上层文件，about/定位到这个文件里的about这样
]