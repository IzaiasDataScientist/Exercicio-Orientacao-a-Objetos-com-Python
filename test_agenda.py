import unittest

from Agenda import Agenda


class MyTestCase(unittest.TestCase):
    def test_something(self):
        obj = Agenda()
        self.assertEqual(obj.armazenaPessoa(nome="Barbara", idade=22, altura=1.56), None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
