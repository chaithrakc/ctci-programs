"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110

Difficulty : Easy
"""


class SolutionCompresser:
    __word = ''

    def set_input(self, word: str) -> None:
        self.__word = word

    def compresser_bruteforce(self) -> str:
        compressed_string = ''
        count_consecutive = 0
        for index in range(len(self.__word)):
            count_consecutive = count_consecutive + 1
            # If next character is different than current, append this char to result.
            if index + 1 >= len(self.__word) or self.__word[index] != self.__word[index + 1]:
                compressed_string += self.__word[index] + str(count_consecutive)
                count_consecutive = 0
        return self.__word if len(self.__word) <= len(compressed_string) else compressed_string
