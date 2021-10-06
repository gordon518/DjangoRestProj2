#from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from blog import SqliDb

def run(request):
    # judge if the request head is json
    if request.content_type != 'application/json':  
        return JsonResponse(data={'err':'only support json data'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    if request.method == 'POST':
        try:
            ret=saveUser(request.data)
            return JsonResponse(data=ret, status=status.HTTP_200_OK)
        except Exception as why:
            print(why.args)
            return JsonResponse(data={'err':why.args}, status=status.HTTP_417_EXPECTATION_FAILED)
    return JsonResponse(data={'err':'request method is not post'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def saveUser(param):
    sqliDb=SqliDb.SqliDb()
    arrParam=[param.get('username'),param.get('password'),param.get('name')]
    ret=sqliDb.exec("insert into user(username,password,name) values (?,?,?)", arrParam)
    return ret
