import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.ftp.staging import *


class MyTestCase(unittest.TestCase):
    def test_encode_asterisk(self):
        self.assertEqual(encode_asterisk("Hello_you!"), "Hello_you!")
        self.assertEqual(encode_asterisk("Hel*o**_"), "Hel_asterisk_o_asterisk__asterisk__")

    def test_decode_asterisk(self):
        self.assertEqual(decode_asterisk("Hello_yo*u!"), "Hello_yo*u!")
        self.assertEqual(decode_asterisk("Hel_asterisk_o_asterisk__asterisk__"), "Hel*o**_")


if __name__ == "__main__":
    _ = unittest.main()
