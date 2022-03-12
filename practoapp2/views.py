from django.http import HttpResponse

def view1(request):
    return HttpResponse('<h1>Welocme</h1>')

def view2(request):
    return HttpResponse('<h1>Welocme from Jagdish</h1>')

def view3(request):
    return HttpResponse('<h1>Just for testing purpose</h1>')