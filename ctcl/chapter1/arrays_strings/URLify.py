def urlify(name: str, true_length: int) -> str:
    char_arr = list(name)
    writer_index = len(name)
    for reader_index in range(true_length - 1, -1, -1):
        if char_arr[reader_index].isspace():
            char_arr[writer_index - 1] = '0'
            char_arr[writer_index - 2] = '2'
            char_arr[writer_index - 3] = '%'
            writer_index = writer_index - 3
        else:
            char_arr[writer_index - 1] = char_arr[reader_index]
            writer_index = writer_index - 1
    return ''.join(char_arr)
