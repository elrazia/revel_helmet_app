import requests
import unittest

class TestApiCall(unittest.TestCase):

    def test_image_post_success(self):
        URL = "http://localhost:8080/api"
        FILE = {"image": open("../hat_selfies/hat1.jpg", 'rb')}
        response = requests.post(url=URL, files=FILE)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()