from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def greeting_view(message):
    def view_fn(request):
        return HttpResponse(message)
    return view_fn

greeting = greeting_view('Good Day')
morning_greeting = greeting_view('Morning to ya')
evening_greeting = greeting_view('Evenign to ya')