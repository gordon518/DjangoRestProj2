#from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
import importlib

# Convention over config, it's stupid to config every url request in "url.py"
# By using this framework, system will call every API modlue's run() function by its path, don't need to config in "url.py" anymore.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def router(request):
    path=request.path_info
    if path[:4]=="/api":
        moduleSrc=path[1:] #get all bytes after first byte
        if moduleSrc[-1:]=="/": #delete last '/'
            moduleSrc=moduleSrc[:-1]
        moduleSrc="blog."+moduleSrc.replace("/",".")
        try:
            lib = importlib.import_module(moduleSrc)
            function=getattr(lib,"run")
            ret=function(request)
        except Exception as why:
            print(why.args)
            ret=JsonResponse(data={'err': why.args}, status=status.HTTP_404_NOT_FOUND)
        return ret

    return JsonResponse(data={'path': path}, status=status.HTTP_200_OK)

