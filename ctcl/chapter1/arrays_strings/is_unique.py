class SolutionUnique:
    __word = ''

    def set_input(self, word: str):
        self.__word = word

    # assuming ascii set has only 128 characters
    # space complexity is high, O(n) time complexity
    def ascii_approach(self, ascii_set=128) -> bool:
        if len(self.__word) > ascii_set:
            return False
        ascii_histogram = [False] * ascii_set
        for char in self.__word:
            ascii_value = ord(char)
            if ascii_histogram[ascii_value]:
                return False
            ascii_histogram[ascii_value] = True
        return True

    # Best Case : O(n) but limited only to lower case letters.
    # space complexity is improved.
    def bitvector(self) -> bool:
        checker = 0
        for char in self.__word:
            bit_index = ord(char) - ord('a')
            if checker & (1 << bit_index) > 0:
                return False
            checker = checker | (1 << bit_index)
        return True

    # worst case : O(n2)
    def bruteforce(self) -> bool:
        for key_index in range(len(self.__word)):
            for other_index in range(key_index + 1, len(self.__word)):
                if self.__word[key_index] == self.__word[other_index]:
                    return False
        return True
