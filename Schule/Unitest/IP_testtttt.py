import unittest
from Schule.Unitest.IP_Aufgabe import *

class IPTest(unittest.TestCase):

    def testCalculation(self):

        self.assertEqual(decimal_to_binary(192), "11000000")
        self.assertEqual(x(11000000), 192)

if __name__ == "__main__":
    unittest.main()