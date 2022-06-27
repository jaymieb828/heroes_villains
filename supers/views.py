from itertools import product
from django.shortcuts import render
import re
from django.shortcuts import get_object_or_404
from logging import raiseExceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response

import supers
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':

        supers_style = request.query_params.get('style')
        print(supers_style)

        
        supers = Supers.objects.all()

        if supers_style:
            supers = supers.filter(supers_style__name=supers_style)

        supers = Supers.objects.all()
        serializer= SupersSerializer(supers, many=True)
        return Response(serializer.data)  
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response(serializer.errors, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
