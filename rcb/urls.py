from django.urls import path
from rcb.views import *

urlpatterns=[
    path('Captain/',Captain,name='Captain'),
]