from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


def test(request):
    return HttpResponse("Url Expaid")


@api_view(['GET'])
def get_person(request):
    data = {}
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True).data
    data['person'] = serializer
    return Response(data, status=status.HTTP_200_OK)

    # return Response("test", status=status.HTTP_200_OK)


@api_view(['POST'])
def insert_person(request):
    data = {}
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the new Karyawan record
        data['msg'] = "Success"
        data['person'] = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    # persons = Person.objects.all()
    # serializer = PersonSerializer(persons, many=True).data
    # data['person'] = serializer
    # return Response(data, status=status.HTTP_200_OK)

    # return Response("test", status=status.HTTP_200_OK)
