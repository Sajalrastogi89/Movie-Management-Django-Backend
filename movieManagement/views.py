from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("This is a dummy response")
