from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from Auth.models import Auth
from Auth.serializers import AuthSerializer


# get list of Auths, save a new Auth, delete all Auths
@csrf_exempt
def auth_list(request):
    if request.method == 'GET':
        auths = Auth.objects.all()
        auth_serializer = AuthSerializer(auths, many=True)
        return JsonResponse(auth_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        auth_data = JSONParser().parse(request)
        auth_serializer = AuthSerializer(data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse(auth_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Very Dangerouse
    # elif request.method == 'DELETE':
    #     Auth.objects.all().delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT)



# get/update/delete auth by ‘id’
@csrf_exempt
def auth_details(request, id):
    try:
        auth = Auth.objects.get(id=id)
    except Auth.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        auth_serializer = AuthSerializer(auth)
        return JsonResponse(auth_serializer.data)

    elif request.method == 'PUT':
        auth_data = JSONParser().parse(request)
        auth_serializer = AuthSerializer(auth, data=auth_data)
        if auth_serializer.is_valid():
            auth_serializer.save()
            return JsonResponse(auth_serializer.data)
        return JsonResponse(auth_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auth.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# find all auth by ‘email’
@csrf_exempt
def auth_by_username(request, user_name):
    auth = Auth.objects.filter(user_name=user_name)

    if request.method == 'GET':
        auth_serializer = AuthSerializer(auth, many=True)
        return JsonResponse(auth_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
