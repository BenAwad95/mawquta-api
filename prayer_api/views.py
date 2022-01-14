from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    print(request)
    return HttpResponse("Good Work, Keep on it💪🏼")
