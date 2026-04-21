"""
URL configuration for lib46 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from .views import *
from .api.views import *
urlpatterns = [

    #add book
    path('Add/',addbook,name='Book_add'),
    #list book
    path('',listbook,name='Book_list'),
    #upate book
    path('<int:id>/Update',bookupdate,name='Book_update'),
    #delerte book
    path('<int:id>/Delete',bookdelete,name='Book_delete'),
    #get book by id
    path('<int:id>',getbookbyid,name='Book_get_id'),
    # path('/Bookjson',getbooksjson,name='getbooksjson')
    # path('api/',include('.api.urls')),
    path('api/',getbooksjson,name='getbooks'),
    path('api/add/',bookadd,name='bookadd'),
]
