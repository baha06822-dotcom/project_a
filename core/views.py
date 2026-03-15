from django.http import HttpResponse


def home(request):
    return HttpResponse("Хули смотришь? Съебался отсюда!")


def health(request):
    return HttpResponse("OK")