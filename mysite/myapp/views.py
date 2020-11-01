from django.http import HttpResponse

def index(request):
    return HttpResponse("HALO BROTHER AND WELCOME!")
