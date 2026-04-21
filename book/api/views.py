from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serlizers import *
from ..models import *
#behvior view --->excuate get,re

@api_view(['POST'])
def bookadd(request):
    objserlizer=BookSerializer(data=request.data)
    if objserlizer.is_valid():
            Book.objects.create(**objserlizer.data)
            return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(data={'data':request.data,'msg':objserlizer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getbooksjson(request):
    books=Book.objects.all()
    bookselizerd=BookSerializer(books,many=True)
    return Response(data=bookselizerd.data,status=status.HTTP_200_OK)


