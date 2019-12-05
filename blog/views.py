from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def greeting(request, message='Good Day'):
    return HttpResponse(message)


def morning_greeting(request):
    return greeting(request, 'Morning to ya')


def evening_greeting(request):
    return greeting(request, 'Evening to ya')