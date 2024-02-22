"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name ="home"),
    path("contact/",views.contact,name="contact"),
    path("plant/",views.plant,name="plant"),
    path("help/",views.help,name="help"),
    path("search/",views.search,name="search"),
    path("detail/<str:name>/",views.compound_detail, name = "detail"),
    path("detail/<str:name>/",views.plant_compound_detail, name = "compounddetail"),
    path('plant/plantdetail/<str:name>/',views.plantviews, name = 'plantdetail'),
    path('detail2/<str:name>/<str:id>/', views.download_sdf, name='download_sdf'), 
    path("advancedsearch/",views.advanced_search,name="advanced_search")

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
