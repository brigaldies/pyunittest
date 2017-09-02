import unittest

from main.py.com.o19s.app import App


class TestCase1(unittest.TestCase):
    def setUp(self):
        self.testcase = 'TestCase1'
        self.app = App(self.testcase)

    def testCase1Method1(self):
        methodName = 'testCase1Method1'
        print(methodName)
        self.assertEqual(self.app.main(), 'Hello {}'.format(self.testcase))

    def testCase1Method2(self):
        methodName = 'testCase1Method2'
        print(methodName)
        self.app.name = methodName
        self.assertEqual(self.app.main(), 'Hello {}'.format(methodName))
