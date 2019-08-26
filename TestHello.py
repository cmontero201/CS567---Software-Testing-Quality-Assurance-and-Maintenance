import unittest

class TestHelloWorld(unittest.TestCase):
    def testHello(self):
        self.assertEqual(2,2,'two equals two')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()