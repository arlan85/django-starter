from django.test import SimpleTestCase

class SalesLogicTests(SimpleTestCase):
    def test_math_library_available(self):
        """Sales dashboard requires numpy for calculations"""
        try:
            import numpy
            imported = True
        except ImportError:
            imported = False

        self.assertTrue(imported, "Numpy is not installed!")
