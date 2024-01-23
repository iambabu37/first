from django.shortcuts import render
from myapp.models import *

def about(request):
    return render(request,"my_app/about.html")

def home(request):
    return render(request,"my_app/home.html")
    
def contact(request):
    return render(request,"my_app/contact.html")

def feed_back(request):
    return render(request,"my_app/feed.html")

def help(request):
    return render(request,"my_app/help.html")

def search(request):
    var = request.GET.get("main_search")
    print(var)
    dict = Plant.objects.all()
    print(dict)
    content = {"dicts":dict}
    print(content)

    return render(request,"my_app/search.html",content)

def compound_detail(request):
    return render (request,"my_app/compound_deatil.html")

