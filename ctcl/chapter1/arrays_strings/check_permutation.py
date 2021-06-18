# using sorting : 2O(nlogn)
def isvalid_permutation_bruteforce(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)


# using ascii : 2O(n) but not space optimized since we will be initializing an array equal to ascii set
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


# using hash tables : 2O(n) and Space Optimized since we use dict and
# initialize only with characters present in both the words
def isvalid_permutation_dicts(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    # letter_counter = dict(Counter(word1)) we can use this line if inbuilt functions are allowed to use
    letter_counter = dict()
    for letter in word1:
        letter_counter[letter] = letter_counter.get(letter, 0) + 1
    for letter in word2:
        letter_counter[letter] = letter_counter.get(letter, 0) - 1
        if letter_counter[letter] < 0:
            return False
    return True
