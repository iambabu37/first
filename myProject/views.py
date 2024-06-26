from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from myapp.models import *
from myapp.forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, FileResponse
import requests
from tempfile import NamedTemporaryFile


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
    

def plant(request):
    obj = Plant.objects.all().order_by("name")
    content = {"dicts":obj}
    return render(request,"my_app/plant.html",content)


def help(request):
    return render(request,"my_app/help.html")



def plantviews(request,name):
   
    obj = get_object_or_404(Plant, name=name)
   
    plantobj = obj.phytochemical_value.all() if obj else None
    # obj2 = plantobj.reference_paper.all() if obj else None
    content = {'dicts':obj,
               "dict2":plantobj}
    print(content)
     
    return render(request,"my_app/plantdetail.html",content)


# function for search 
def search(request):
    
    var = request.GET.get("main_search","").strip()
    print(var)
    page_number = request.GET.get('page',1)
    if not var or var.isspace():
        messages.error(request, 'Please enter a valid search term.')
        return render(request, "my_app/search.html")
    # dict = Plant.objects.all().order_by("name")
    dicts = Phytochemical.objects.filter(
         Q(synonymous_names__icontains = var ) &
         Q(synonymous_names__istartswith =var) 
     ).order_by("name")
    print(dicts)
    if not dicts:
        messages.info(request, 'No results found.')
    
    paginator = Paginator(dicts, 10)  # Show 10 plants per page
    page_number = request.GET.get('page')
    print(page_number)
    print(request.GET)
    final_data = paginator.get_page(page_number)

    # try: 
    #     plant_page = paginator.page(final_data)
    # except PageNotAnInteger:
    #     plant_page = paginator.page(1)
    # except EmptyPage:
    #     plant_page = paginator.page(paginator.num_pages)

    content = {"dicts": final_data}

    return render(request, "my_app/search.html", content)
    
    # content = {"dicts":dict}

    # return render(request,"my_app/search.html",content)


#function for compound details

def compound_detail(request,name):
    
    phytochemical_instance = Phytochemical.objects.get(name=name)
    
    content ={"dicts":phytochemical_instance}
    print(content)    
    return render (request,"my_app/compound_detail.html",content)

def plant_compound_detail(request,name):
    
    phytochemical_instance = get_object_or_404(Phytochemical, name=name)
    
    content ={"dicts":phytochemical_instance}
    print(content)    
    return render (request,"my_app/compound_detail.html",content)

def download_sdf(request, name,id):
    # PubChem URL for the compound with the given name
    print(f"{name}")
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{id}/record/SDF/"

    # Fetch SDF content from PubChem
    response = requests.get(pubchem_url)

    if response.status_code == 200:
        sdf_content = response.content

        # Create a temporary file and write the SDF content
        with NamedTemporaryFile(delete=False, suffix='.sdf') as tmp_file:
            tmp_file.write(sdf_content)
            tmp_file_path = tmp_file.name

        # Set the response content type to force a download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{name}.sdf"'

        # Write the file content to the response
        with open(tmp_file_path, 'rb') as file:
            response.write(file.read())

        # Delete the temporary file
        os.remove(tmp_file_path)

        return response

    return HttpResponse(f"Error fetching SDF content for compound name {name} from PubChem")

def advanced_search(request):
     
     return render(request,"my_app/acknowledgement.html")

def target(request,name):
     obj = get_object_or_404(Target,name = name)
     content = {"dicts":obj}
     return render(request,"my_app/target.html",content)
     