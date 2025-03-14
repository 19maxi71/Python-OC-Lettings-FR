from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='US'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_lettings_index(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lettings')
        self.assertContains(response, 'Test Letting')

    def test_letting_detail(self):
        url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, 'Test Street')
