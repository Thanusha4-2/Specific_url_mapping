from django.urls import path
from csk.views import *

urlpatterns=[
    path('Captain/',Captain,name='Captain'),
]
