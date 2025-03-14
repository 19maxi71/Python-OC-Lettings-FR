from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
import logging


class ProfileTest(TestCase):
    def setUp(self):
        """Set up test data and disable logging during tests"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )
        # Disable logging during tests
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        """Re-enable logging after tests"""
        logging.disable(logging.NOTSET)

    def test_profiles_index(self):
        """Test profiles index page loads correctly"""
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profiles')
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail(self):
        """Test profile detail page loads correctly"""
        url = reverse('profiles:profile', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test City')
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_404(self):
        """Test non-existent profile returns 404"""
        url = reverse('profiles:profile', kwargs={'username': 'nonexistent'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_index_database_error(self):
        """
        Test database error handling in index view.
        Simulate database error by deleting all profiles
        """
        Profile.objects.all().delete()
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
