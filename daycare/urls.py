"""
URL configuration for daycare_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from daycare import views
from daycare.views import imara_mall_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('babysitters/', views.babysitters, name='babysitters'),
    path('emily_carter/', views.emily_carter, name='emily_carter'),
    path('james_lee/', views.james_lee, name='james_lee'),
    path('sarah_jonson/', views.sarah_jonson, name='sarah_jonson'),
    path('book_sarah_modal/', views.book_sarah_modal, name='book_sarah_modal'),
    path('programs/', views.programs, name='programs'),
    path('westlands_location/', views.westlands_location, name='westlands_location'),
    path('imara_mall_location/', imara_mall_location, name='imara_mall_location'),
    path('calendar/', views.calendar, name='calendar'),
    path('menu/', views.menu, name='menu'),
    path('programs/infant/', views.infant, name='infant'),
    path('toddler/', views.toddler, name='toddler'),
    path('preschool/', views.preschool, name='preschool'),
    path('extended/', views.extended, name='extended'),
    path('/enrollment/', views.enrollment, name='enrollment'),
    path('enrolled/',views.enrolled, name='enrolled'),
    path('approved/<int:id>/', views.approved, name='approved'),
    path('events/', views.events, name='events'),
    path('approved/', views.approved, name='approved'),

    path('babysitters_list/', views.babysitters_list, name='babysitters_list'),
    path('babysitters/approve/<int:id>/', views.approve_babysitter, name='approve_babysitter'),



]
