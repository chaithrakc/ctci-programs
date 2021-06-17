from collections import Counter


def are_permutations(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    return dict(Counter(word1)) == dict(Counter(word2))


