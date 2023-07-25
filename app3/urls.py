from django.urls import path
from app3.views import *
urlpatterns=[
    path('first/',first,name='first'),
     path('second/',second,name='second'),
]