import unittest
from unittest.mock import patch, Mock
from githubAPI import getUserHistory
# docs for mock and patch: https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods

class TestGetUserHistory(unittest.TestCase):
    @patch('githubAPI.requests.get') # defines the object to be mocked 
    def test_successful_request(self, mockGet):
        mockResponse = Mock()
        mockResponse.status_code = 200
        mockResponse.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        mockGet.return_value = mockResponse

        result = getUserHistory('test_user')

        self.assertEqual(result, [('repo1', 2), ('repo2', 2)])

    @patch('githubAPI.requests.get')
    def test_failed_request(self, mockGet):
        mockResponse = Mock()
        mockResponse.status_code = 404
        mockGet.return_value = mockResponse

        result = getUserHistory('test_user')

        self.assertEqual(result, [])

    @patch('githubAPI.requests.get')
    def test_invalid_input(self, mockGet):
        mockResponse = Mock()
        mockResponse.status_code = 200
        mockResponse.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        mockGet.return_value = mockResponse

        result = getUserHistory(1)

        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
