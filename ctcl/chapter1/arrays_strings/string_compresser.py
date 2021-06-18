def compressor_bruteforce(decomp: str):
    compressed_char = list()
    compressed_count = list()
    index = -1
    for char in decomp:
        if index == -1 or char not in compressed_char[index]:
            index = index + 1
            compressed_count.insert(index, 1)
            compressed_char.insert(index, char)
        else:
            compressed_count[index] = compressed_count[index] + 1
    return get_compressed_string(compressed_char, compressed_count, decomp)


def get_compressed_string(characters: list, counter: list, decomp: str) -> str:
    compressed_str = ''
    for index in range(len(characters)):
        compressed_str = compressed_str + characters[index] + str(counter[index])
    if len(decomp) <= len(compressed_str):
        return decomp
    return compressed_str
