
"""
Module to generate and validate HashCash stamps.

"""

__author__ = 'per'


from hashlib import sha1
from datetime import datetime
from random import randint
from math import ceil

rand_chars = ([chr(x) for x in range(ord('a'), ord('z'))] +
              [chr(x) for x in range(ord('A'), ord('Z'))] +
              [chr(x) for x in range(ord('0'), ord('9'))] +
              ['+', '-', '/'])


char_map = {'0' : '0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111'}


rc_len = len(rand_chars)


def verify(nbits, stamp):

    if nbits < 32:
        val = int(sha1(stamp).hexdigest()[0:8], base=16)
        return val <= (0xFFFFFFFF >> nbits)

    else:
        val = ''.join(char_map[x] for x in sha1(stamp).hexdigest()[:int(ceil(float(nbits)/4))])
        return val.startswith(''.join('0' for x in range(0, nbits)))


def generate(nbits, resource):
    # ver:bits:date:resource:[ext]:rand:counter
    ver = 1
    bits = nbits
    date_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    ext = ''
    rand = ''.join(rand_chars[randint(0, rc_len-1)] for x in range(0, 10))
    counter = 0

    result = None
    while result is None:
        stamp = ":".join(str(elem) for elem in [ver, bits, date_str, ext, rand, counter])

        if verify(nbits, stamp):
            result = stamp
            break

        counter += 1

    return result


if __name__ == "__main__":
    
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument("NBITS", type=int, default=15, help="Number of leading zeroes in a stamp")
    parser.add_argument("RESOURCE", help="The resource string to use in the stamp. Ex: email address, ip address, etc")
    parser.add_argument('-v', '--verify', action='store_true', help="Verify RESOURCE as a HashCash stamp")
    
    args = parser.parse_args()

    action = 'generate'
    
    if args.verify:
        action = 'verify'

    print(locals()[action](args.NBITS, args.RESOURCE))
