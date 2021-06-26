class SolutionPermutation:
    __first_word = ''
    __second_word = ''

    def set_input(self, first_word: str, second_word: str):
        self.__first_word = first_word
        self.__second_word = second_word

    # using sorting : 2O(nlogn)
    def isvalid_anagram_bruteforce(self) -> bool:
        if len(self.__first_word) != len(self.__second_word):
            return False
        return sorted(self.__first_word) == sorted(self.__second_word)

    # using ascii : 2O(n) but not space optimized since we will be initializing an array equal to ascii set
    def isvalid_anagram_ascii(self, ascii_set=128) -> bool:
        if len(self.__first_word) != len(self.__second_word):
            return False
        letters = [0] * ascii_set
        for char in self.__first_word:
            ascii_val = ord(char)
            letters[ascii_val] = letters[ascii_val] + 1
        for char in self.__second_word:
            ascii_val = ord(char)
            letters[ascii_val] = letters[ascii_val] - 1
            if letters[ascii_val] < 0:
                return False
        return True

    # using hash tables : 2O(n) and Space Optimized since we use dict and initialize only with characters present in
    # both the words
    def isvalid_anagram_optimized(self) -> bool:
        if len(self.__first_word) != len(self.__second_word):
            return False
        letter_counter = dict()  # letter_counter = dict(Counter(self.__first_word))  if inbuilt functions are allowed
        for letter in self.__first_word:
            letter_counter[letter] = letter_counter.get(letter, 0) + 1
        for letter in self.__second_word:
            letter_counter[letter] = letter_counter.get(letter, 0) - 1
            if letter_counter[letter] < 0:
                return False
        return True
