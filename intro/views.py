from django.http import HttpResponse

def hello(request):
    return HttpResponse ( "Hello World" )


def witaj (request):
    return HttpResponse ("Witaj RAFAŁ")
