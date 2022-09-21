from django.http import HttpResponse


def home(request):
    return HttpResponse('Home2')


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')