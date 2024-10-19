import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def test_get_request(self):
        # Simulating a GET request
        with app.test_request_context('/hello', method='GET'):
            response = app.full_dispatch_request()
            assert response.data == b'Hello, GET request!'

    def test_post_request(self):
        # Simulating a POST request
        with app.test_request_context('/hello', method='POST', data={'name': 'Alice'}):
            response = app.full_dispatch_request()
            assert response.data == b'Hello, Alice!'

if __name__ == '__main__':
    unittest.main()
