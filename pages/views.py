from django.http import HttpResponse

# Create your views here.

def homeView(request):
    return HttpResponse('Hello, World!')