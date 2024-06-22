from django.test import TestCase

# Create your tests here.
class ExampleTestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpTestData: Run once to set up data for all class method.')

    def setUp(self):
        print('setUp: Run once for every test method.')

    def test_false(self):
        print('Test method: test_false')
        self.assertFalse(True)

    def test_add(self):
        print('Test method: test_add')
        result = 1 + 1
        self.assertEqual(result,3)