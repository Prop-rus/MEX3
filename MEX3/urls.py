"""MEX3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MEX3app import forms, views
from django.conf.urls import include

admin.autodiscover()

urlpatterns = [
    path('', views.Home_view, name = 'home'),
    path('admin/', admin.site.urls),
    path('form/', views.Form_view, name = 'form'),
    path('form1/', views.Form1_view, name = 'form1'),
    path('form2/', views.Form2_view, name = 'form2'),
    path('form3/', views.Form3_view, name = 'form3'),
    path('sendfile/', views.getResultFilesFromDisk, name ='sendfile'),
    path('sendexample/<form_num>', views.getExampleFiles,  name ='send_example'),


]
