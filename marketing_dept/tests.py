from django.test import SimpleTestCase
from django.urls import reverse

class MarketingViewTests(SimpleTestCase):
    def test_marketing_index_content(self):
        """Check that the marketing page contains the word 'Marketing'"""
        # This uses the 'namespace' we set up earlier
        url = reverse('marketing:index')
        response = self.client.get(url)
        self.assertContains(response, "Marketing")
