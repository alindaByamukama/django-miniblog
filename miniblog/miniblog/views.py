from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! Welcome to my Home page.")

def about(request):
    return HttpResponse("My About page")