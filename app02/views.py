from django.shortcuts import render, HttpResponse
from django.urls import reverse
# Create your views here.
def login(request):
    return HttpResponse("APP02")

def app_namespace_url(request):
    pat = reverse('app02:app_namespace_url')
    print(pat)
    return HttpResponse("app02 app_namespace_url")