
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

    def test_invalid_nbits_raises_ValueError(self):

        with self.assertRaises(ValueError):
            hashcash.validate(-1, 'blah')

        with self.assertRaises(ValueError):
            hashcash.validate(3000, 'blah')

    def test_validate_known_stamps(self):

        assert(hashcash.is_valid("1:48:110416:etienne@cri.fr:::000A2F00000063BF012"))
        assert(hashcash.is_valid("1:44:070217:foo::xSi0bPjoswUh6h1Y:TMNI7"))
        assert(hashcash.is_valid("1:42:060922:When I think of all the good times that I've wasted ...::UXkz/DsCCgfvBVtH:00000EF7+j"))
        assert(hashcash.is_valid("1:40:051222:foo@bar.org::Cu2iqc4SmotZ7MRR:0000214c3J"))
