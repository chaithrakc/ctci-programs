'''
String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
Hints: #34, #88, # 704

Difficulty : Easy
'''


class SolutionStringRotation:
    __first_string = ''
    __second_string = ''

    def set_input(self, first_string: str, second_string: str) -> None:
        self.__first_string = first_string
        self.__second_string = second_string

    def __is_substring(self, string: str, sub_string: str) -> bool:
        return True if string.find(sub_string) > -1 else False

    def are_rotated(self) -> bool:
        # Check that sl and s2 are equal length and not empty
        if len(self.__first_string) == len(self.__second_string) and len(self.__first_string) > 0:
            repeated_first_str = self.__first_string * 2
            return self.__is_substring(repeated_first_str, self.__second_string)
        return False
