"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #7 7 7, #732

Difficulty: Easy

"""


class SolutionUnique:
    word = ''

    def set_input(self, word: str) -> None:
        self.word = word

    # assuming ascii set has only 128 characters
    # space complexity is high, O(n) time complexity
    def ascii_approach(self, ascii_set=128) -> bool:
        # if len(self.word) > ascii_set:
        #     return False
        # ascii_histogram = [False] * ascii_set
        # for char in self.word:
        #     ascii_value = ord(char)
        #     if ascii_histogram[ascii_value]:
        #         return False
        #     ascii_histogram[ascii_value] = True
        # return True
        hashset = set()
        for char in self.word:
            if char in hashset:
                return False
            hashset.add(char)
        return True

    # Best Case : O(n) but limited only to lower case letters.
    # space complexity is improved.
    def bitvector(self) -> bool:
        checker = 0
        for char in self.word:
            bit_index = ord(char) - ord('a')
            if checker & (1 << bit_index) > 0:
                return False
            checker = checker | (1 << bit_index)
        return True

    # worst case : O(n2)
    def bruteforce(self) -> bool:
        for key_index in range(len(self.word)):
            for other_index in range(key_index + 1, len(self.word)):
                if self.word[key_index] == self.word[other_index]:
                    return False
        return True
