import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import *

class Command(BaseCommand):
    help = 'Import data from Excel sheet into Django model'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']

        try:
            df = pd.read_excel(excel_file_path)

            for index, row in df.iterrows():
                # Assuming YourModel has fields like 'field1', 'field2', etc.
                Phytochemical.objects.create(
                    name = row["Phytochemical name"],
                    synonymous_names = row[""],
                    smiles = row[""],
                    chem_image= row[""],
                    inchi = row[""],
                    inchikey = row[""],
                    deepsmile= row[""],
                    functional_groups = row[""]
                )
                # McProp.objects.create(
                #     name= row['Phytochemical name'],
                #     kegg = row["kegg_id"],
                #     molecular_formula = row["molecular_formula"],
                #     iupac_name = row["chemical_name"],
                #     molecular_weight = row["Molecular weight (g/mol)"],
                #     Molprot =row["Molprot"],
                #     pubchem = row["pubchem"],
                #     surecheml= row["surecheml"],
                #     impaat = row["Phytochemical id "][2:],
                #     chembl = row["chembl"],
                #     zinc = row["zinc"],
                #     log_p=row['Log P'],
                #     topological_polar_surface_area=row["Topological polar surface area"],
                #     num_hydrogen_bond_acceptors=row["Number of hydrogen bond acceptors"],
                #     hydrogen_donor=row["Number of hydrogen bond donors"],
                #     num_carbon_atoms=row["Number of carbon atoms"],
                #     num_heavy_atoms=row["Number of heavy atoms"],
                #     num_heteroatoms=row["Number of heteroatoms"],
                #     num_nitrogen_atoms=row["Number of nitrogen atoms"],
                #     num_sulfur_atoms =row["Number of sulfur atoms"],
                #     num_chiral_carbon_atoms=row["Number of chiral carbon atoms"],
                #     stereochemical_complexity=row["Stereochemical complexity"],
                #     num_sp_hybridized_carbon_atoms=row["Number of sp hybridized carbon atoms"],
                #     num_sp2_hybridized_carbon_atoms=row["sp2_atoms"],
                #     num_sp3_hybridized_carbon_atoms = row["sp3_atoms"],
                #     shape_complexity=row['Shape complexity'],
                #     num_rotatable_bonds=row["Number of rotatable bonds"],
                #     num_aliphatic_carbocycles=row["Number of aliphatic carbocycles"],
                #     num_aliphatic_heterocycles=row['Number of aliphatic heterocycles'], 
                #     num_aliphatic_rings=row["Number of aliphatic rings"],
                #     num_aromatic_carbocycles=row["Number of aromatic carbocycles"],
                #     num_aromatic_heterocycles = row["Number of aromatic heterocycles"],
                #     num_aromatic_rings =row["Number of aromatic rings"],
                #     total_num_rings = row["Total number of rings"],
                #     num_saturated_carbocycles =row["Number of saturated carbocycles"],
                #     num_saturated_heterocycles = row["Number of saturated heterocycles"],
                #     num_saturated_rings = row["Number of saturated rings"],
                #     num_sssr = row["Number of Smallest Set of Smallest Rings (SSSR)"]
                #     #reference_detail=row["References"]
                # )
                # DkProp.objects.create(
                #     name= row['Phytochemical name'],
                #     lipinski_violations= row["Lipinski’s rule of 5 filter"],
                #     lipinski_rule = row["Number of Lipinski"],
                #     ghose_violations = row["Number of Ghose filter violations"],
                #     veber_rule = row["Veber"],
                #     ghose_rule = row["Ghose_rule"],
                #     gsk_4_400_rule = row["GSK"],
                #     pfizer_3_75_rule = row["Pfizer"],
                #     qedw_score = row["QEDw_ score"]

                # )
                # ADMEProp.objects.create(
                    
                #     name= row['Phytochemical name'],
                #     bioavailability_score = row["Bioavailability score"],
                #     solubility_class_esol = row["Solubility class [ESOL]"],
                #     solubility_class_silicos_it = row["Solubility class [Silicos-IT]"],
                #     blood_brain_barrier_permeation = row["Blood Brain Barrier permeation"],
                #     gastrointestinal_absorption = row["Gastrointestinal absorption"],
                #     log_kp_skin_permeation = row["Log K"],
                #     num_pains_structural_alerts = row["Number of PAINS structural alerts"],
                #     num_brenk_structural_alerts = row["Number of Brenk structural alerts"],
                #     cyp1a2_inhibitor = row["CYP1A2 inhibitor"],
                #     cyp2c19_inhibitor = row["CYP2C19 inhibitor"],
                #     cyp2c9_inhibitor = row["CYP2C9 inhibitor"],
                #     cyp2d6_inhibitor = row["CYP2D6 inhibitor"],
                #     cyp3a4_inhibitor = row["CYP3A4 inhibitor"],
                #     p_glycoprotein_substrate = row["P-glycoprotein substrate"]




                # )

            self.stdout.write(self.style.SUCCESS('Data import successful'))

        except pd.errors.EmptyDataError as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {e}. The Excel file is empty.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing data: {e}'))