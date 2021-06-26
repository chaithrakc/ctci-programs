class SolutionCompressor:
    __decom_str = ''

    def set_input(self, decompressed: str):
        self.__decom_str = decompressed

    def compressor_bruteforce(self):
        compressed_char = list()
        compressed_count = list()
        index = -1
        for char in self.__decom_str:
            if index == -1 or char not in compressed_char[index]:
                index = index + 1
                compressed_count.insert(index, 1)
                compressed_char.insert(index, char)
            else:
                compressed_count[index] = compressed_count[index] + 1
        return self.__get_compressed_string(compressed_char, compressed_count)

    def __get_compressed_string(self, characters: list, counter: list) -> str:
        compressed_str = ''
        for index in range(len(characters)):
            compressed_str = compressed_str + characters[index] + str(counter[index])
        if len(self.__decom_str) <= len(compressed_str):
            return self.__decom_str
        return compressed_str
