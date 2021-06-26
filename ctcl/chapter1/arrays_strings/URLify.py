class SolutionURLify:
    __name = ''
    __true_length = 0

    def set_input(self, name: str, true_length: int) -> None:
        self.__name = name
        self.__true_length = true_length

    def urlify(self) -> str:
        char_arr = list(self.__name)
        writer_index = len(self.__name)
        for reader_index in range(self.__true_length - 1, -1, -1):
            if char_arr[reader_index].isspace():
                char_arr[writer_index - 1] = '0'
                char_arr[writer_index - 2] = '2'
                char_arr[writer_index - 3] = '%'
                writer_index = writer_index - 3
            else:
                char_arr[writer_index - 1] = char_arr[reader_index]
                writer_index = writer_index - 1
        return ''.join(char_arr)
