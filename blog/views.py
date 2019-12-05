from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class GreetingView(View):

    message = 'Good Day' #클래스 변수

    def get(self, *args, **kwargs):
        return HttpResponse(self.message)


greeting = GreetingView.as_view()

class MorningGreetingView(GreetingView):
    message = 'Morning to ya'

morning_greeting = MorningGreetingView.as_view()

evening_greeting = GreetingView.as_view(message='Evening to ya')

