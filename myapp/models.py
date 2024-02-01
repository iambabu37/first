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
    synonymous_names = models.TextField()
    external_identifiers = models.TextField()
    smiles = models.TextField()
    inchi = models.TextField()
    inchikey = models.TextField()
    deepsmiles = models.TextField()
    functional_groups = models.TextField()
    classyfire_kingdom = models.CharField(max_length=255)
    classyfire_superclass = models.CharField(max_length=255)
    classyfire_class = models.CharField(max_length=255)
    classyfire_subclass = models.CharField(max_length=255)
    np_classifier_biosynthetic_pathway = models.TextField()
    np_classifier_superclass = models.CharField(max_length=255)
    np_classifier_class = models.CharField(max_length=255)
    np_likeness_score = models.FloatField()
    
   
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

class DruglikenessProperties(models.Model):
    phytochemical = models.OneToOneField(Phytochemical, on_delete=models.CASCADE)
    lipinski_violations = models.IntegerField()
    lipinski_rule = models.IntegerField()
    ghose_violations = models.IntegerField()
    veber_rule = models.CharField()
    ghose_rule = models.CharField()
    gsk_4_400_rule = models.BooleanField()
    pfizer_3_75_rule = models.BooleanField()
    qedw_score = models.FloatField()

    def __str__(self):
        return " DrukLikeness "

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=254, validators=[EmailValidator(message='Enter a valid email address.')])
    phone_no = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message='Enter a valid phone number.')])
    message = models.TextField()
    time_of_submit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MolecularProperties(models.Model):
    molecular_weight = models.FloatField()
    log_p = models.FloatField()
    topological_polar_surface_area = models.FloatField()
    num_hydrogen_bond_acceptors = models.IntegerField()
    num_hydrogen_bond_donors = models.IntegerField()
    num_carbon_atoms = models.IntegerField()
    num_heavy_atoms = models.IntegerField()
    num_heteroatoms = models.IntegerField()
    num_nitrogen_atoms = models.IntegerField()
    num_sulfur_atoms = models.IntegerField()
    num_chiral_carbon_atoms = models.IntegerField()
    stereochemical_complexity = models.FloatField()
    num_sp_hybridized_carbon_atoms = models.IntegerField()
    num_sp2_hybridized_carbon_atoms = models.IntegerField()
    num_sp3_hybridized_carbon_atoms = models.IntegerField()
    shape_complexity = models.FloatField()
    num_rotatable_bonds = models.IntegerField()
    num_aliphatic_carbocycles = models.IntegerField()
    num_aliphatic_heterocycles = models.IntegerField()
    num_aliphatic_rings = models.IntegerField()
    num_aromatic_carbocycles = models.IntegerField()
    num_aromatic_heterocycles = models.IntegerField()
    num_aromatic_rings = models.IntegerField()
    total_num_rings = models.IntegerField()
    num_saturated_carbocycles = models.IntegerField()
    num_saturated_heterocycles = models.IntegerField()
    num_saturated_rings = models.IntegerField()
    num_sssr = models.IntegerField()

    def __str__(self):
        return f"Molecular Properties for compound ID: {self.id}"

from django.db import models

class ADMEProperties(models.Model):
    bioavailability_score = models.FloatField()
    solubility_class_esol = models.CharField(max_length=255)
    solubility_class_silicos_it = models.CharField(max_length=255)
    blood_brain_barrier_permeation = models.BooleanField()
    gastrointestinal_absorption = models.BooleanField()
    log_kp_skin_permeation = models.FloatField()
    num_pains_structural_alerts = models.IntegerField()
    num_brenk_structural_alerts = models.IntegerField()
    cyp1a2_inhibitor = models.BooleanField()
    cyp2c19_inhibitor = models.BooleanField()
    cyp2c9_inhibitor = models.BooleanField()
    cyp2d6_inhibitor = models.BooleanField()
    cyp3a4_inhibitor = models.BooleanField()
    p_glycoprotein_substrate = models.BooleanField()

    def __str__(self):
        return f"ADME Properties for compound ID: {self.id}"
