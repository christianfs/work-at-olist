from unittest import TestCase
from api.app import create_app


class TestCallRecords(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.client = self.app.test_client()

    def test_health_check_with_succes(self):
        response = self.client.get('/api/health')
        assert response.status_code == 200
