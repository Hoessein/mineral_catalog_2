from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def test_course_creation(self):
        """tests if Mineral model is created and asserts the name attribute of it"""
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
        """Tests if the data of json file is added to the db
        and asserts if the data amount is equal to the amount in the db"""
        Mineral.json_to_db()
        mineral_amount = Mineral.objects.count()
        self.assertEqual(mineral_amount, 874)


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
        """tests the home view"""
        resp = self.client.get(reverse('minerals:minerals_home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertContains(resp, self.mineral)

    def test_detail_view(self):
        """tests the detail view"""
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_detail_404(self):
        """tests if 404 error is thrown"""
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': 98432}))
        self.assertEqual(resp.status_code, 404)

    def test_random_detail_view(self):
        """tests the random detail view"""
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertRedirects(resp, '/detail/1/', status_code=302, target_status_code=200)
