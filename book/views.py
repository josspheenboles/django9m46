from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse

from .forms import BookForm,BookFormModel
from .models import Book
from catagory.models import Catagory

# Create your views here.
#function basded view
#param of httprequest
#return object httpresponse




# @api_view(['GET','POST'])
def addbook(request):
    #document.write
    # return HttpResponse('<h1>add new boook</h1>')
    context={}
    # print(request.method)
    # print(request.POST)
    # print(request.GET)

    if request.method=='GET':
        context['cats']=Catagory.objects.all()
        context['form']=BookFormModel()
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
        #publish form data
        form=BookFormModel(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Book.objects.create(
            #     name=form.cleaned_data['name'],
            #     version=form.cleaned_data['version'],
            #              price=form.cleaned_data['price'],
            #              description=form.cleaned_data['description'],
            #              catagory=
            #              Catagory.objects.get(pk=form.cleaned_data['catagory']))
            form.save()
        else:
            context['cats'] = Catagory.objects.all()
            context['form'] = BookFormModel(request.POST)
            context['msg']=form.errors
            return render(request, 'book/add.html', context)
        #redirect book list
        return HttpResponseRedirect('/Book/')
        # return HttpResponse('<h1>add new boook</h1>')

def listbook(req):
    return render(req,'book/list.html',{'books':
                                        Book.objects.all()})
    # return HttpResponse('<h1>list book</h1>')

def getbookbyid(request,id):
    # print(type(request))
    # return HttpResponse(f'<h1>get book by {id}  </h1>')
    context={'book':Book.objects.get(id=id)}
    return render(request,'book/bookdetails.html',context)
def bookupdate(request,id):
    if request.method=='GET':
        context={'form':BookFormModel(instance=Book.objects.get(id=id))}
    # print(type(request))
    # return HttpResponse(f'<h1>update book by {id}  </h1>')
        return render(request, 'book/update.html', context)
    else:
        form=BookFormModel(request.POST,instance=Book.objects.get(id=id)    )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Book/')
        else:
            context={'form':form,'msg':form.errors}
            return render(request, 'book/update.html', context)
def bookdelete(request,id):
    print(type(request))
    return HttpResponse(f'<h1>Delete book by {id}  </h1>')


