from django.urls import path
from .views import *
urlpatterns = [
    path('',getbooksjson,name='getbooks'),

    ]