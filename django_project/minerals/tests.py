from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral


class CourseModelTests(TestCase):
    def test_course_creation(self):
        mineral=Mineral.objects.create(
            name='name',
            image_filename='image filename',
            image_caption='image caption',
            category='category',
            formula='formula',
            strunz_classification='strunz classification',
            crystal_system='crystal system',
            unit_cell='unit cell',
            color='color',
            crystal_symmetry='crystal symmetry',
            cleavage='cleavage',
            mohs_scale_hardness='mohs scale hardness',
            luster='luster',
            streak='streak',
            diaphaneity='diaphaneity',
            optical_properties='optical properties',
            refractive_index='refractive index',
            crystal_habit='crystal habit',
            specific_gravity='specific gravity',
            group='group'
    )
        self.assertEqual(mineral.name, 'namadfadfe')