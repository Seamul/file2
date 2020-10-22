
from django.urls import path, re_path
from . import views

# namespace
app_name = 'file_download'

urlpatterns = [

    path('file_download/', views.file_download, name='file_download'),

]