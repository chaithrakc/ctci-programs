class SolutionPalindromePermutation:
    __phrase = ''

    def set_iput(self, phrase: str) -> None:
        self.__phrase = phrase

    def isvalid_palindrome_permutation_dicts(self) -> bool:
        self.__phrase = str.lower(self.__phrase)  # to make case insensitive
        self.__phrase = self.__phrase.replace(' ', '')  # removing the spaces
        letter_count = self.__build_charfreq_table()
        return self.__check_maxone_odd(letter_count)

    def __build_charfreq_table(self) -> list:
        freq_table = [0] * (ord('z') - ord('a') + 1)
        for char in self.__phrase:
            index = ord(char) - ord('a')
            freq_table[index] = freq_table[index] + 1
        return freq_table

    def __check_maxone_odd(self, table: list) -> bool:
        odd_counter = False  # check whether all letters have even count except for at most one letter.
        for count in table:
            if count % 2:
                if odd_counter:
                    return False
                odd_counter = True
        return True

    def isvalid_palindrome_permutation_bitvector(self) -> bool:
        phrase = str.lower(self.__phrase)  # to make case insensitive
        phrase = phrase.replace(' ', '')  # removing the spaces
        bitvector = 0
        for letter in phrase:
            val = ord(letter) - ord('a')
            bitvector = bitvector ^ (1 << val)
        return bin(bitvector).count('1') == len(
            phrase) % 2  # all letters have even count zero except for at most one letter
