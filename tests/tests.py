import requests
import unittest

class TestApiCall(unittest.TestCase):

    def test_server_running(self):
        URL = "http://localhost:8080/"
        response = requests.get(url=URL)
        self.assertEqual(response.status_code,200)
        
    def test_image_post_success(self):
        ''' Posts an image to localhost:8080/api endpoint.
            Checks to see if response is a success.'''
        URL = "http://localhost:8080/api"
        FILE = {"image": open("../images/hat_selfies/hat1.jpg", 'rb')}
        response = requests.post(url=URL, files=FILE)
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()