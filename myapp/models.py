from django.db import models
from django.core.validators import EmailValidator,RegexValidator
import datetime,os
from django.contrib.postgres.fields import ArrayField

# Create your models here.
def img_plant(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/plant",new_file)

def img_chem(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/chem",new_file)

class Phytochemical(models.Model):
    name = models.CharField(max_length=255)
    struture = models.TextField()
    molecular_weight = models.FloatField()
    formula = models.CharField(max_length=255)
    disease_association = models.CharField(max_length= 255)
    bioactivity = models.CharField(max_length=255)
    struture_image= models.ImageField(upload_to=img_chem)
    plant_source = models.ForeignKey("plant",on_delete=models.CASCADE,related_name = "phyto")
    description_compound = models.TextField()
    time_of_add = models.DateTimeField(auto_now_add= True)
   
    def __str__(self):
        return self.name
    
class Plant(models.Model):
    name = models.CharField(max_length=255)
    botanical_name = models.CharField(max_length = 255)
    family = models.CharField(max_length = 255)
    active_compound = models.CharField(max_length=255)
    related_diseae = models.CharField(max_length = 255)
    plant_image = models.ImageField(upload_to=img_plant)
    part_used = models.CharField(max_length = 255)
    description = models.TextField()
    time_of_add_plant = models.DateTimeField(auto_now_add= True)
    reference_detail = ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, null=True, size=None)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254, validators=[EmailValidator(message='Enter a valid email address.')])
    phone_no = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message='Enter a valid phone number.')])
    message = models.TextField()
    time_of_submit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


