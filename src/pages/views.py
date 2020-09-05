from django.http import HttpResponse
from django.shortcuts import render
#https://docs.djangoproject.com/en/3.1/ref/templates/builtins/ template tags use in variable in \templates
# Create your views here.
def home_view(request,*args , **kwargs):
    print(args , kwargs)
    print(request.user)
    return render(request,"home.html",{})
    # return HttpResponse("<h1>Hello World</h1>") #String of HTML code

def contact_view(request,*args , **kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args , **kwargs):
    my_context = {
        "title"    : "this is about us",
        "my_number"  : 123,
        "my_list"    : [123,234,345,"Nawata Mute"] 
    }
    return render(request,"about.html",my_context)

def social_view(request,*args , **kwargs):
    return HttpResponse("<h1>Social Page</h1>")