def ascii_approach(word: str, ascii_set=128) -> bool:
    if len(word) > ascii_set:
        return False
    ascii_histogram = [False] * ascii_set
    for char in word:
        ascii_value = ord(char)
        if ascii_histogram[ascii_value]:
            return False
        ascii_histogram[ascii_value] = True
    return True


def bitvector(word: str) -> bool:
    checker = 0
    for char in word:
        bit_index = ord(char) - ord('a')
        if checker & (1 << bit_index) > 0:
            return False
        checker = checker | (1 << bit_index)
    return True


def bruteforce(word: str) -> bool:
    for key_index in range(len(word)):
        for other_index in range(key_index + 1, len(word)):
            if word[key_index] == word[other_index]:
                return False
    return True
