
import unittest
import hashcash

class HashcashTests(unittest.TestCase):

    def setUp(self):
        self.test_str = '0xdeadbeef'
        self.nbits = 5

    def test_generate_utf8(self):

        stamp = hashcash.generate(self.nbits, self.test_str, encoding='utf-8')
        assert(hashcash.validate(self.nbits, stamp, encoding='utf-8') is True)

    def test_generate_latin1(self):

        stamp = hashcash.generate(self.nbits, self.test_str, encoding='latin-1')
        assert(hashcash.validate(self.nbits, stamp, encoding='latin-1') is True)
