from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from catagory.models import Catagory
# Create your views here.
#function basded view
#param of httprequest
#return object httpresponse
def addbook(request):
    #document.write
    # return HttpResponse('<h1>add new boook</h1>')
    context={}
    # print(request.method)
    # print(request.POST)
    # print(request.GET)
    if request.method=='GET':
        context['cats']=Catagory.objects.all()
        return  render(request,'book/add.html',context)
    else:
        #save data
        # bookobj=Book(name=request.POST['name'],
        #              version=request.POST['version'],
        #              price=request.POST['price'],
        #              description=request.POST['description'],
        #              catagory=
        #              Catagory.objects.get(pk=request.POST['catagoryid']))
        # bookobj.save()
        Book.objects.create(
            version=request.POST['version'],
                         price=request.POST['price'],
                         description=request.POST['description'],
                         catagory=
                         Catagory.objects.get(pk=request.POST['catagoryid']))

        #redirect book list
        return HttpResponse('<h1>add new boook</h1>')

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