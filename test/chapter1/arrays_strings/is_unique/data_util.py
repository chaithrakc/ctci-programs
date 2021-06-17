import random
import string


def get_testdata():
    long_str = random.choice(string.ascii_letters) * 130
    return [
        ('Abacus', True),
        ('chaithra', False),
        ('asdfghjkl', True),
        ('123456776', False),
        (long_str, False)
    ]


def get_testdata_bitvector():
    return [
        ('chaithra', False),
        ('asdfghjkl', True),
    ]
