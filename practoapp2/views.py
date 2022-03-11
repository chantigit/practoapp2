from django.http import HttpResponse

def view1(request):
    return HttpResponse('<h1>Welocme</h1>')
