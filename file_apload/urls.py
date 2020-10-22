from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('base/',views.file_upload,name='upload')
]