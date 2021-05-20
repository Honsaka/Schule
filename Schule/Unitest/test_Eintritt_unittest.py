import unittest
from Unitest.Eintritt import eintritt


class EintrittTest(unittest.TestCase):

    def testCalculation(self):

        self.assertEqual(eintritt(0), 0)
        self.assertEqual(eintritt(3), 0)
        self.assertEqual(eintritt(4), 6)
        self.assertEqual(eintritt(12), 6)
        self.assertEqual(eintritt(67), 8)
        self.assertEqual(eintritt(100), 8)
        self.assertEqual(eintritt(13), 12)
        self.assertEqual(eintritt(66), 12)

if __name__ == "__main__":
    unittest.main()

    self.assertEqual(x(11000000), 192)
    self.assertEqual(x(27), 11111111 - 11111111 - 11111111 - 11100000)
    self.assertEqual(x(192 - 168 - 111 - 100), 11000000 - 10101000 - 01101111 - 01100100)
    self.assertEqual(x(11000000 - 10101000 - 01101111 - 01100100), 192 - 168 - 111 - 100)