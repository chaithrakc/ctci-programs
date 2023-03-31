'''
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737
'''
class SolutionPermutation:
    first_word = ''
    second_word = ''

    def set_input(self, first_word: str, second_word: str) -> None:
        self.first_word = first_word
        self.second_word = second_word

    # using sorting : 2O(nlogn)
    def isvalid_anagram_bruteforce(self) -> bool:
        if len(self.first_word) != len(self.second_word):
            return False
        return sorted(self.first_word) == sorted(self.second_word)

    # using ascii : 2O(n) but not space optimized since we will be initializing an array equal to ascii set
    def isvalid_anagram_ascii(self, ascii_set=128) -> bool:
        if len(self.first_word) != len(self.second_word):
            return False
        letters = [0] * ascii_set
        for char in self.first_word:
            ascii_val = ord(char)
            letters[ascii_val] = letters[ascii_val] + 1
        for char in self.second_word:
            ascii_val = ord(char)
            letters[ascii_val] = letters[ascii_val] - 1
            if letters[ascii_val] < 0:
                return False
        return True

    # using hash tables : 2O(n) and Space Optimized since we use dict and initialize only with characters present in
    # both the words
    def isvalid_anagram_optimized(self) -> bool:
        if len(self.first_word) != len(self.second_word):
            return False
        letter_counter = dict()  # letter_counter = dict(Counter(self.__first_word))  if inbuilt functions are allowed
        for letter in self.first_word:
            letter_counter[letter] = letter_counter.get(letter, 0) + 1
        for letter in self.second_word:
            letter_counter[letter] = letter_counter.get(letter, 0) - 1
            if letter_counter[letter] < 0:
                return False
        return True
