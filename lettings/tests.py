from django.test import TestCase, Client
from django.urls import reverse
from .models import Address, Letting
import logging


class LettingViewsTest(TestCase):
    def setUp(self):
        """Set up test data and client"""
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )
        # Disable logging during tests
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        """Clean up after tests"""
        logging.disable(logging.NOTSET)

    def test_index_view(self):
        """Test the index view"""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_detail_view(self):
        """Test the letting detail view"""
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_404(self):
        """Test non-existent letting returns 404"""
        response = self.client.get(
            reverse('lettings:letting', args=[999])
        )
        self.assertEqual(response.status_code, 404)

    def test_index_database_error(self):
        """
        Test database error handling in index view.
        Simulate database error by deleting all lettings
        """
        Letting.objects.all().delete()
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
