from django.db import models
from django.core.validators import EmailValidator,RegexValidator
import datetime,os
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
def img_plant(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/plant",new_file)

def img_chem(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/chem",new_file)


class Reference(models.Model):
    reference = models.CharField(max_length=255,null = True,blank=True)
    title = models.CharField(max_length = 255,null = True, blank= True)
    def __str__(self):
        return self.title
    




class Contact(models.Model):
    name = models.CharField(max_length=50,null = True,blank=True)
    email = models.CharField(max_length=254, validators=[EmailValidator(message='Enter a valid email address.')])
    phone_no = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message='Enter a valid phone number.')])
    message = models.TextField(null = True,blank=True)
    time_of_submit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class McProp(models.Model):
    molecular_weight = models.FloatField(null = True,blank=True)
    log_p = models.FloatField(null = True,blank=True)
    topological_polar_surface_area = models.FloatField(null = True,blank=True)
    num_hydrogen_bond_acceptors = models.IntegerField(null = True,blank=True)
    num_hydrogen_bond_donors = models.IntegerField(null = True,blank=True)
    num_carbon_atoms = models.IntegerField(null = True,blank=True)
    num_heavy_atoms = models.IntegerField(null = True,blank=True)
    num_heteroatoms = models.IntegerField(null = True,blank=True)
    num_nitrogen_atoms = models.IntegerField(null = True,blank=True)
    num_sulfur_atoms = models.IntegerField(null = True,blank=True)
    num_chiral_carbon_atoms = models.IntegerField(null = True,blank=True)
    stereochemical_complexity = models.FloatField(null = True,blank=True)
    num_sp_hybridized_carbon_atoms = models.IntegerField(null = True,blank=True)
    num_sp2_hybridized_carbon_atoms = models.IntegerField(null = True,blank=True)
    num_sp3_hybridized_carbon_atoms = models.IntegerField(null = True,blank=True)
    shape_complexity = models.FloatField(null = True,blank=True)
    num_rotatable_bonds = models.IntegerField(null = True,blank=True)
    num_aliphatic_carbocycles = models.IntegerField(null = True,blank=True)
    num_aliphatic_heterocycles = models.IntegerField(null = True,blank=True)
    num_aliphatic_rings = models.IntegerField(null = True,blank=True)
    num_aromatic_carbocycles = models.IntegerField(null = True,blank=True)
    num_aromatic_heterocycles = models.IntegerField(null = True,blank=True)
    num_aromatic_rings = models.IntegerField(null = True,blank=True)
    total_num_rings = models.IntegerField(null = True,blank=True)
    num_saturated_carbocycles = models.IntegerField(null = True,blank=True)
    num_saturated_heterocycles = models.IntegerField(null = True,blank=True)
    num_saturated_rings = models.IntegerField(null = True,blank=True)
    num_sssr = models.IntegerField(null = True,blank=True)

    def __str__(self):
        return f"Molecular Properties for compound ID: {self.id}"



class ADMEProp(models.Model):
    bioavailability_score = models.FloatField(null = True,blank=True)
    solubility_class_esol = models.CharField(max_length=255,null = True,blank=True)
    solubility_class_silicos_it = models.CharField(max_length=255,null = True,blank=True)
    blood_brain_barrier_permeation = models.BooleanField(null = True,blank=True)
    gastrointestinal_absorption = models.BooleanField(null = True,blank=True)
    log_kp_skin_permeation = models.FloatField(null = True,blank=True)
    num_pains_structural_alerts = models.IntegerField(null = True,blank=True)
    num_brenk_structural_alerts = models.IntegerField(null = True,blank=True)
    cyp1a2_inhibitor = models.BooleanField(null = True,blank=True)
    cyp2c19_inhibitor = models.BooleanField(null = True,blank=True)
    cyp2c9_inhibitor = models.BooleanField(null = True,blank=True)
    cyp2d6_inhibitor = models.BooleanField(null = True,blank=True)
    cyp3a4_inhibitor = models.BooleanField(null = True,blank=True)
    p_glycoprotein_substrate = models.BooleanField(null = True,blank=True)

    def __str__(self):
        return f"ADME Properties for compound ID: {self.id}"
        
class DkProp(models.Model):
    lipinski_violations = models.IntegerField(null = True,blank=True)
    lipinski_rule = models.IntegerField(null = True,blank=True)
    ghose_violations = models.IntegerField(null = True,blank=True)
    veber_rule = models.CharField(max_length=255,null = True,blank=True)
    ghose_rule = models.CharField(max_length=255,null = True,blank=True)
    gsk_4_400_rule = models.BooleanField(null = True,blank=True)
    pfizer_3_75_rule = models.BooleanField(null = True,blank=True)
    qedw_score = models.FloatField(null = True,blank=True)

    def __str__(self):
        return f" DrukLikeness{self.id} "

    
class Phytochemical(models.Model):
    name = models.CharField(max_length=255,null = True,blank=True)
    synonymous_names = models.TextField(null = True,blank=True)
    molecular_formula = models.TextField(null = True,blank=True)
    smiles = models.TextField(null = True,blank=True)
    pubchem_id = models.IntegerField(null =True,blank=True)
    chem_image = models.ImageField(upload_to=img_chem,null = True,blank=True)
    inchi = models.TextField(null = True,blank=True)
    inchikey = models.TextField(null = True,blank=True)
    deepsmiles = models.TextField(null = True,blank=True)
    functional_groups = models.TextField(null = True,blank=True)
    classyfire_kingdom = models.CharField(max_length=255,null = True,blank=True)
    classyfire_superclass = models.CharField(max_length=255,null = True,blank=True)
    classyfire_class = models.CharField(max_length=255,null = True,blank=True)
    classyfire_subclass = models.CharField(max_length=255,null = True,blank=True)
    np_classifier_biosynthetic_pathway = models.TextField(null = True,blank=True)
    np_classifier_superclass = models.CharField(max_length=255,null = True,blank=True)
    np_classifier_class = models.CharField(max_length=255,null = True,blank=True)
    np_likeness_score = models.FloatField(null = True,blank=True)
    mkproperties = models.OneToOneField(McProp, on_delete=models.CASCADE ,blank =True,null=True )
    dkproperties = models.OneToOneField(DkProp,on_delete = models.CASCADE,blank=True,null=True)
    admeproperties = models.OneToOneField(ADMEProp,on_delete = models.CASCADE,blank=True,null =True)
    reference_paper = models.ManyToManyField( Reference,blank=True)

    def __str__(self):
        return self.name


    
class Plant(models.Model):
    name = models.CharField(max_length=255,null = True,blank=True)
    botanical_name = models.CharField(max_length = 255,null = True,blank=True)
    family = models.CharField(max_length = 255,null = True,blank=True)
    synonyms = models.CharField(max_length=255,null= True,blank=True)
    groups = models.CharField(max_length=255,null = True,blank=True)
    related_plant = models.CharField(max_length = 255,null = True,blank=True)
    related_diseae = models.CharField(max_length = 255,null = True,blank=True)
    plant_image = models.ImageField(upload_to=img_plant,null = True,blank=True)
    description = models.TextField(null = True,blank=True)
    time_of_add_plant = models.DateTimeField(auto_now_add= True)
    phytochemical_value = models.ManyToManyField(Phytochemical ,blank = True)
    referenceplant = models.ManyToManyField( Reference, blank = True)

    def __str__(self):
        return self.name