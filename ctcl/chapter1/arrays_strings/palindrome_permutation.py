def isvalid_palindrome_permutation_dicts(phrase: str) -> bool:
    phrase = str.lower(phrase)  # to make case insensitive
    phrase = phrase.replace(' ', '')  # removing the spaces
    letter_count = build_charfreq_table(phrase)
    return check_maxone_odd(letter_count)


def build_charfreq_table(phrase: str) -> list:
    freq_table = [0] * (ord('z') - ord('a') + 1)
    for char in phrase:
        index = ord(char) - ord('a')
        freq_table[index] = freq_table[index] + 1
    return freq_table


def check_maxone_odd(table: list) -> bool:
    odd_counter = False  # check whether all letters have even count except for at most one letter.
    for count in table:
        if count % 2:
            if odd_counter:
                return False
            odd_counter = True
    return True


def isvalid_palindrome_permutation_bitvector(phrase: str) -> bool:
    phrase = str.lower(phrase)  # to make case insensitive
    phrase = phrase.replace(' ', '')  # removing the spaces
    bitvector = 0
    for letter in phrase:
        val = ord(letter) - ord('a')
        bitvector = bitvector ^ (1 << val)
    return bin(bitvector).count('1') == len(phrase) % 2  # all letters have even count zero except for at most one letter
