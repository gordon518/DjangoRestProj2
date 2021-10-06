#from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

def run(request):
    return JsonResponse(data={'err':None}, status=status.HTTP_200_OK)

