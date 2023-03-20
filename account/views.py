from django.http import HttpResponse

# Create your views here.

def Signup(request):
    return HttpResponse("<h1>guess you want to signup?</h1>")



def Login(request):
    return HttpResponse("<h1>guess you want to login?</h1>")
