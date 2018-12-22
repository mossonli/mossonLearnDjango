from django.shortcuts import render,HttpResponse

# Create your views here.

def special_case_2003(request):
    # request 是封装的请求对象
    print(request)
    print(request.GET)
    return HttpResponse("OK")

def login(request):

    return render(request, 'login.html')
