def isvalid_palindrome_permutation_dicts(word: str) -> bool:
    word = str.lower(word)  # to make case insensitive
    word = word.replace(' ', '')  # removing the spaces
    letter_count = dict()
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    odd_counter = False  # check whether all letters have even count except for at most one letter.
    for letter in word:
        if letter_count.get(letter) % 2:
            if odd_counter:
                return False
            odd_counter = True
    return True
