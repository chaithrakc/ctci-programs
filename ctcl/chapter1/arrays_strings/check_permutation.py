from collections import Counter


# using hash tables : 3O(n)
def isvalid_permutation_dicts(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    return dict(Counter(word1)) == dict(Counter(word2))


# using sorting : 2O(nlogn)
def isvalid_permutation_bruteforce(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)


# using ascii : 2O(n) but not space optimized
def isvalid_permutation_optimized(word1: str, word2: str, ascii_set=128) -> bool:
    if len(word1) != len(word2):
        return False
    letters = [0] * ascii_set
    for char in word1:
        ascii_val = ord(char)
        letters[ascii_val] = letters[ascii_val] + 1

    for char in word2:
        ascii_val = ord(char)
        letters[ascii_val] = letters[ascii_val] - 1
        if letters[ascii_val] < 0:
            return False
    return True
