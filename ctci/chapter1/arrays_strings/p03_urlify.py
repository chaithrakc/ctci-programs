'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Hints: #53, # 118
'''
class SolutionURLify:
    name = ''
    true_length = 0

    def set_input(self, name: str, true_length: int) -> None:
        self.name = name
        self.true_length = true_length

    def urlify(self) -> str:
        char_arr = list(self.name)
        writer_index = len(self.name)
        for reader_index in range(self.true_length - 1, -1, -1):
            if char_arr[reader_index].isspace():
                char_arr[writer_index - 1] = '0'
                char_arr[writer_index - 2] = '2'
                char_arr[writer_index - 3] = '%'
                writer_index = writer_index - 3
            else:
                char_arr[writer_index - 1] = char_arr[reader_index]
                writer_index = writer_index - 1
        return ''.join(char_arr)
