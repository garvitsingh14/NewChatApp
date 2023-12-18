from django.urls import path
from home.views import *

urlpatterns = [
    # path('<str:group_name>/',index,name="index" ),
    path('demo/',demo,name="demo" ),
]