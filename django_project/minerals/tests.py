from django.urls import reverse
from django.test import TestCase
from unittest.mock import ANY


from .models import Mineral


class MineralModelTests(TestCase):
    def test_course_creation(self):
        """tests if Mineral model is created and asserts the name attribute of it"""
        mineral=Mineral.objects.create(
            name='Abelsonite',
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
            group='Other'
    )
        self.assertEqual(mineral.name, 'Abelsonite')


class MineralsViewsTests(TestCase):

    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Abelsonite',
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
            group='Other'
        )

    def test_home_view(self):
        """tests the home view"""
        resp = self.client.get(reverse('minerals:minerals_home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertContains(resp, 'Search')
        self.assertContains(resp, self.mineral)

    def test_detail_view(self):
        """tests the detail view"""
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Diaphaneity')
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_detail_404(self):
        """tests if 404 error is thrown"""
        resp = self.client.get(reverse('minerals:mineral_detail', kwargs={'pk': 98432}))
        self.assertEqual(resp.status_code, 404)

    def test_group_view(self):
        resp = self.client.get(reverse('minerals:group_mineral', kwargs={'group_name': self.mineral.group}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertContains(resp, 'Other')

    def test_alphabet_view(self):
        resp = self.client.get(reverse('minerals:alphabet', kwargs={'letter': 'a'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertContains(resp, self.mineral.name)
        self.assertNotContains(resp, 'Zunyite')

    def test_search_view(self):
        resp = self.client.get(reverse('minerals:search_mineral'), {'q': 'Abelsonite'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/list.html')
        self.assertContains(resp, self.mineral.name)
        self.assertNotContains(resp, 'Zunyite')

    def test_random_detail_view(self):
        """tests the random detail view"""
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertRedirects(resp, '/detail/1/', status_code=302, target_status_code=200)












