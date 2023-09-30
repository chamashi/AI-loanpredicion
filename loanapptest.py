import unittest
import json
from loanapp import app

class TestLoanApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a clean database or use a testing database
        cls.app = app.test_client()
        cls.app.testing = True

    @classmethod
    def tearDownClass(cls):
        # Clean up resources or perform database teardown (if needed)
        pass

    def setUp(self):
        # Set up the database for each test (if needed)
        pass

    def tearDown(self):
        # Clean up after each test (if needed)
        pass

    def test_customer_registration(self):
        # Define test data for customer registration
        test_data = {
            'email': 'exo@example.com',
            'name': 'exo user',
            'password': 'exo123',
        }

        # Send a POST request to the registration endpoint
        response = self.app.post('/register', json=test_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON and check for the success message
        data = json.loads(response.data.decode('utf-8'))
        actual_message = data.get('message', '').strip()  # Remove leading/trailing whitespace
        expected_message = 'Registration successful'

        self.assertEqual(actual_message, expected_message)

    def test_customer_login(self):
        # Define test data for customer login
        test_data = {
            'email': 'exo@example.com',
            'password': 'exo123',
        }

        # Send a POST request to the login endpoint
        response = self.app.post('/login', json=test_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON and check for the success message
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'Customer logged in successfully')

    def test_customer_registration_duplicate_email(self):
        # Define test data for duplicate email registration
        test_data = {
            'email': 'exo@example.com',
            'name': 'exo user',
            'password': 'exo123',
        }

        # Send a POST request to the registration endpoint
        response = self.app.post('/register', json=test_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON and check for the error message
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['error'], 'Email is already registered')

if __name__ == '__main__':
    unittest.main()
