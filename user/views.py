from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from user.models import MainUser


# Create your views here.

@api_view(['POST'])
def signup(request):
    print(request.body)
    return JsonResponse({"Hello": "World"})
