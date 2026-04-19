from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#function basded view
#param of httprequest
#return object httpresponse
def addbook(request):
    #document.write
    # return HttpResponse('<h1>add new boook</h1>')
    context={'msg':'from add book'}
    return  render(request,'add.html',contetxt)

def listbook(req):
    return HttpResponse('<h1>list book</h1>')

def getbookbyid(request,id):
    print(type(request))
    return HttpResponse(f'<h1>get book by {id}  </h1>')
def bookupdate(request,id):
    print(type(request))
    return HttpResponse(f'<h1>update book by {id}  </h1>')
def bookdelete(request,id):
    print(type(request))
    return HttpResponse(f'<h1>Delete book by {id}  </h1>')