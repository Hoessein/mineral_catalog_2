from django.db import models
import json


class Mineral(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255)
    cleavage = models.CharField(max_length=255)
    mohs_scale_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255)
    crystal_habit = models.CharField(max_length=255)
    specific_gravity = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def json_to_db(cls):
        with open('minerals.json', encoding='utf8') as file:
            data = json.load(file)
            for mineral in data:
                try:
                    Mineral(
                        name=mineral['name'],
                        image_filename=mineral['image filename'],
                        image_caption=mineral['image caption'],
                        category=mineral['category'],
                        formula=mineral['formula'],
                        strunz_classification=mineral['strunz classification'],
                        crystal_system=mineral['crystal system'],
                        unit_cell=mineral['unit cell'],
                        color=mineral['color'],
                        crystal_symmetry=mineral['crystal symmetry'],
                        cleavage=mineral['cleavage'],
                        mohs_scale_hardness=mineral['mohs scale hardness'],
                        luster=mineral['luster'],
                        streak=mineral['streak'],
                        diaphaneity=mineral['diaphaneity'],
                        optical_properties=mineral['optical properties'],
                        refractive_index=mineral['refractive index'],
                        crystal_habit=mineral['crystal habit'],
                        specific_gravity=mineral['specific gravity']
                    ).save()
                except KeyError:
                    pass

