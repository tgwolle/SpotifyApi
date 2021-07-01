import unittest
from spotifyproj import auth


class TestFileName(unittest.TestCase):
    def test_auth(self):
        self.assertEqual(auth(), 200)



if __name__ == '__main__':
    unittest.main()