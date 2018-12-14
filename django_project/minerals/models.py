from django.db import models


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
