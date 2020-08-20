import unittest
import numSave

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app = numSave.create_app()
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        result = self.app.get('/')
        print(result)
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()