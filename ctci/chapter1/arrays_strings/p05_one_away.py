'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
Hints:#23, #97, #130
'''
class SolutionOneEditAway:
    __first_word = ''
    __second_word = ''

    def set_input(self, first_word, second_word) -> None:
        self.__first_word = first_word
        self.__second_word = second_word

    def one_editaway(self) -> bool:
        if len(self.__first_word) == len(self.__second_word):
            return self.__valid_replace()
        elif len(self.__first_word) + 1 == len(self.__second_word):
            return self.__valid_insert()
        elif len(self.__first_word) - 1 == len(self.__second_word):
            self.__first_word, self.__second_word = self.__second_word, self.__first_word  # swapping values
            return self.__valid_insert()
        return False

    def __valid_replace(self) -> bool:
        found_difference = False
        for index in range(len(self.__first_word)):
            if self.__first_word[index] != self.__second_word[index]:
                if found_difference:
                    return False
                found_difference = True
        return True

    def __valid_insert(self) -> bool:
        short_word_index = 0
        long_word_index = 0
        while long_word_index < len(self.__second_word) and short_word_index < len(self.__first_word):
            if self.__first_word[short_word_index] != self.__second_word[long_word_index]:
                if short_word_index != long_word_index:
                    return False
                long_word_index = long_word_index + 1
            else:
                short_word_index = short_word_index + 1
                long_word_index = long_word_index + 1
        return True
