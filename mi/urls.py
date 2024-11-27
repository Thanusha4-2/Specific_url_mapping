from django.urls import path
from mi.views import *

urlpatterns=[
    path('Captain/',Captain,name='Captain'),
]