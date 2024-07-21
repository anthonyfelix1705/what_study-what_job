"""
URL configuration for my_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('registeration.html',views.registeration),
   
    path('home/tenth',views.tenth),
    path('home/Commerce',views.Commerce),
    path('home/home.html',views.science),
    path('home/Science',views.science),
    path('home/physics',views.physics),
    path('home/chemistry',views.chemistry),
    path('home/Biology',views.biology),
    path('home/Mathematics',views.mathematics),
    path('home/Computer',views.computer),
    path('home/home',views.home),
    path('home/arts',views.arts),
    path('home/',views.home),
    path('home/Economic',views.Economic),
    path('home/Accounts',views.Accounts),
    path('home/Business',views.Business),
    path('home/Geography',views.Geography),
    path('home/Language',views.Language),
    path('home/History',views.History),
    path('home/Psychology',views.Psychology),
    path('home/Sociology',views.Sociology),
    path('home/Literature',views.Literature),
    path('home/Political',views.Political),
    path('home/Professional',views.Professional),
    path('home/aftertwelth',views.aftertwelth),
    path('home/aarts',views.aarts),
    path('home/acommerce',views.acommerce),
    path('home/ascience',views.ascience),
    path('home/medical',views.medical),
    path('home/design',views.design),
    path('home/law',views.law),
    path('home/hotel',views.hotel),
    path('home/osc',views.osc),
    path('home/vocational',views.vocational),
    path('home/aftercollege',views.aftercollege),
    path('home/government',views.government),
    path('home/upsc',views.upsc),
    path('home/tnpsc',views.tnpsc),
    path('home/ssc',views.ssc),
    path('home/artsjob',views.artsjob),
    path('home/commercejob',views.commercejob),
    path('home/medicaljob',views.medicaljob),
    path('home/designjob',views.designjob),
    path('home/engineeringjob',views.engineeringjob),
    path('home/itjob',views.itjob),
    path('home/diplomajob',views.diplomajob),
    path('home/sciencejob',views.sciencejob),
]
