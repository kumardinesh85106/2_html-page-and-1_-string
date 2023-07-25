from django.urls import path
from app2.views import *
app='anything'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]