from django.test import SimpleTestCase
from django.apps import apps

class EngineeringConfigTests(SimpleTestCase):
    def test_app_is_registered(self):
        """Check if the engineering_dept app is properly installed in settings.py"""
        self.assertTrue(apps.is_installed('engineering_dept'))

    def test_app_name_is_correct(self):
        """Check if the app config has the expected name"""
        self.assertEqual(apps.get_app_config('engineering_dept').name, 'engineering_dept')
