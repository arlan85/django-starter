from django.test import SimpleTestCase, Client

class DashboardRoutingTests(SimpleTestCase):
    def setUp(self):
        # The Client acts like a dummy web browser
        self.client = Client()

    def test_root_url_404(self):
        """The root URL should return a 404 because no view is mapped to '/'"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_department_pages_resolve(self):
        """Check that all department endpoints return a 200 OK"""
        departments = ['/engineering/', '/marketing/', '/sales/']

        for route in departments:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(
                    response.status_code, 200,
                    msg=f"Route {route} failed to resolve."
                )
