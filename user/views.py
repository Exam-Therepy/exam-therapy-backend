import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from user.models import MainUser


# Create your views here.

@api_view(['POST'])
def signup(request):
    response = {}
    try:
        body = request.body
        dictData = json.loads(body)
        user, created = MainUser.objects.get_or_create(**dictData)
        if not created:
            response['status_code'] = status.HTTP_409_CONFLICT
            response['message'] = "User already exist"
        elif not user:
            response['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response['message'] = "Something went wrong"
        else:
            response['status_code'] = status.HTTP_201_CREATED
            response['message'] = "Sign up successfully"

    except Exception as e:
        response['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response['message'] = str(e)
    return JsonResponse(response, status=response['status_code'])
