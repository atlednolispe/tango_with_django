from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the rango index."
                        "<br/>"
                        "<a href='/rango/about'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page."
                        "<br/>"
                        "<a href='/rango/'>Rango</a>"
                        )
