from django.urls import path
from app1.views import *
app='something'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]