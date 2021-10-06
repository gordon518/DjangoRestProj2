#from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from blog import SqliDb

def run(request):
    # judge if the request head is json
    if request.method == 'POST':
        if request.content_type != 'application/json':  
            return JsonResponse(data={'err':'only support json data'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        try:
            ret=saveBlog(request)
            return JsonResponse(data=ret, status=status.HTTP_200_OK)
        except Exception as why:
            print(why.args)
            return JsonResponse(data={'err':why.args}, status=status.HTTP_417_EXPECTATION_FAILED)

    elif request.method == 'GET':
        ret=queryBlog(request)
        return JsonResponse(data=ret, status=status.HTTP_200_OK)
    return JsonResponse(data={'err':'request method not supported'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def saveBlog(request):
    ret={'err':None}
    if request.session.get('userid')==None:
        return {'err':"You haven't logged in!"}
    param=request.data
    sqliDb=SqliDb.SqliDb()
    arrParam=[param.get('title'),param.get('body'),request.session['userid']]
    ret=sqliDb.exec("insert into blog(title,body,owner) values (?,?,?)", arrParam)
    return ret

def queryBlog(request):
    param=request.query_params.dict()
    ssql="select a.*,b.username from blog a join user b on a.owner=b.id"
    swhere=""
    arrParam=[]
    if param.get('title')!=None:
        swhere=" where a.title=?"
        arrParam.append(param.get('title'))
    if param.get('body')!=None:
        if len(swhere)==0:
            swhere=' where a.body=?'
        else:
            swhere+=' and a.body=?'
        arrParam.append(param.get('body'))
    if param.get('ownerName')!=None:
        if len(swhere)==0:
            swhere=' where b.username=?'
        else:
            swhere+=' and b.username=?'
        arrParam.append(param.get('ownerName'))
    
    sqliDb=SqliDb.SqliDb()
    ret=sqliDb.query(ssql+swhere, arrParam)
    return ret
