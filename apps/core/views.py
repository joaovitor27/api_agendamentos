from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Workstations, Reservation
from .serializer import WorkstationsSerializer, ReservationSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@csrf_exempt
def reservation(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        get_reservation = Reservation.objects.all()
        serializer = ReservationSerializer(get_reservation, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def reservation_pk(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    try:
        get_reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return JsonResponse('error', status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReservationSerializer(get_reservation, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        get_reservation.delete()
        return JsonResponse("SUCESSO", status=201, safe=False)


@csrf_exempt
def workstations(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        get_workstations = Workstations.objects.all()
        serializer = WorkstationsSerializer(get_workstations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WorkstationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def workstations_pk(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    try:
        get_workstations = Workstations.objects.get(pk=pk)
    except Workstations.DoesNotExist:
        return JsonResponse('error', status=status.HTTP_404_NOT_FOUND, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WorkstationsSerializer(get_workstations, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        get_workstations.delete()
        return JsonResponse("SUCESSO", status=201, safe=False)
