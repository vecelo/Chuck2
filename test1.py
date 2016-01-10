import unittest
from f1 import kiem

class tc1(unittest.TestCase):
    def setUp(self):
        pass

    def test_f1(self):
        self.assertEqual(kiem(['<key>Track ID</key>'],['<integer>369</integer>']), 369)

if __name__ == '__main__':
    unittest.main()