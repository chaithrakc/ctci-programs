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
            if index+1 >= len(self.__word) or self.__word[index] != self.__word[index + 1]:
                compressed_string += self.__word[index] + str(count_consecutive)
                count_consecutive = 0
        return self.__word if len(self.__word) <= len(compressed_string) else compressed_string
