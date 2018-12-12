from django.db import models
import json

class Mineral(models.Model):
    name = models.CharField(max_length=500)
    image_filename = models.CharField(max_length=500)
    image_caption = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    formula = models.CharField(max_length=500)
    strunz_classification = models.CharField(max_length=500)
    color = models.CharField(max_length=500)
    crystal_system = models.CharField(max_length=500)
    unit_cell = models.CharField(max_length=500)
    crystal_symmetry = models.CharField(max_length=500)
    cleavage = models.CharField(max_length=500)
    mohs_scale_hardness = models.CharField(max_length=500)
    luster = models.CharField(max_length=500)
    streak = models.CharField(max_length=500)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=500)
    refractive_index = models.CharField(max_length=500)
    crystal_habit = models.CharField(max_length=500)
    specific_gravity = models.CharField(max_length=500)
    group = models.CharField(max_length=500)

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
                        image_filename=mineral.get('image filename', ""),
                        image_caption=mineral.get('image caption', ""),
                        category=mineral.get('category',""),
                        formula=mineral.get('formula', ""),
                        strunz_classification=mineral.get('strunz classification', ""),
                        crystal_system=mineral.get('crystal system', ""),
                        unit_cell=mineral.get('unit cell', ""),
                        color=mineral.get('color', ""),
                        crystal_symmetry=mineral.get('crystal symmetry', ""),
                        cleavage=mineral.get('cleavage', ""),
                        mohs_scale_hardness=mineral.get('mohs scale hardness', ""),
                        luster=mineral.get('luster', ""),
                        streak=mineral.get('streak', ""),
                        diaphaneity=mineral.get('diaphaneity', ""),
                        optical_properties=mineral.get('optical properties', ""),
                        refractive_index=mineral.get('refractive index', ""),
                        crystal_habit=mineral.get('crystal habit', ""),
                        specific_gravity=mineral.get('specific gravity', ""),
                        group=mineral.get('group')
                    ).save()
                except KeyError:
                    continue
