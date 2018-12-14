from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral


class MineralModelTests(TestCase):
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
        self.assertEqual(mineral.name, 'name')

    def test_json_to_db(self):
        Mineral.json_to_db()
        min = Mineral.objects.count()
        self.assertEqual(min, 874)


class MineralsViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
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


    def test_home_view(self):
        resp = self.client.get(reverse('minerals:minerals_home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertContains(resp, self.mineral)

    def test_detail_view(self):
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_random_detail_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects()
