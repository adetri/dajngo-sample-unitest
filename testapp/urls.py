from django.urls import path, include
from django.contrib import admin
from .views import *
app_name = 'testapp'

urlpatterns = [

    path('', test, name='create_category'),
    path('getperson', get_person, name='get_person'),
    path('insertperson', insert_person, name='insertperson'),






]
