import pytest

from ctcl.chapter1.arrays_strings.string_compresser import compressor_bruteforce


def get_testcases():
    test_cases = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcd', 'abcd'),
        ('ABCDDE', 'ABCDDE'),
        ('aaaaaaBccDZZ', 'a6B1c2D1Z2')
    ]
    return test_cases


@pytest.mark.parametrize('decompressed, compressed', get_testcases())
def test_compress_string(decompressed, compressed):
    assert compressor_bruteforce(decompressed) == compressed
