from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import template


def index(request):
    return render(request, "index.html")
def news(request):
    return render(request, "news.html")
def guids(request):
    return render(request, "guids.html")
def matches(request):
    return render(request, "matches.html")
def tournaments(request):
    return render(request, "tournaments.html")

