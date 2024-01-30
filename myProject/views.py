from django.shortcuts import render,redirect
from django.db.models import Q
from myapp.models import *
from myapp.forms import *
from django.contrib import messages

def about(request):
    return render(request,"my_app/about.html")

def home(request):
    return render(request,"my_app/home.html")

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()  # Save the data to the database
			return redirect('home')  # Redirect to a success page
	return render(request, 'my_app/contact.html')
    

def feed_back(request):
    return render(request,"my_app/feed.html")

def help(request):
    return render(request,"my_app/help.html")

def search(request):
    
    var = request.GET.get("main_search") if request.GET.get != None else " "
    print(var)
    if not var or var.isspace():
        messages.error(request, 'Please enter a valid search term.')
        return render(request, "my_app/search.html")
    
    dict = Plant.objects.filter(
         Q(name__icontains = var) &
         Q(name__istartswith =var) 
     )
   
    if not dict:
        messages.info(request, 'No results found.')
    
    content = {"dicts":dict}

    return render(request,"my_app/search.html",content)

def compound_detail(request,name):
    
    dict = Plant.objects.filter(name=name)
    content ={"dict":dict}
    return render (request,"my_app/compound_detail.html",content)

