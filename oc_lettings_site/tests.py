from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
import logging


class OCLettingsSiteTest(TestCase):
    def setUp(self):
        """Set up test client and disable logging during tests"""
        self.client = Client()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        """Re-enable logging after tests"""
        logging.disable(logging.NOTSET)

    def test_index_view(self):
        """Test main index page loads correctly"""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_404_handler(self):
        """Test custom 404 page"""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_500_handler(self):
        """Test custom 500 page"""
        with self.assertRaises(Exception) as context:
            self.client.get(reverse('test-500'))
        self.assertEqual(str(context.exception), 'Testing 500 page')

    def test_sentry_debug_view(self):
        """Test Sentry error reporting"""
        url = reverse('trigger_error')
        with self.assertRaises(ZeroDivisionError):
            self.client.get(url)
