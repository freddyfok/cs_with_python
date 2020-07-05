"""
rabin karp algorithm is rolling hashing algo for pattern matching
especially with finding substring in a text
what you do is to compare the hash numbers
and then compare the actual words

hashing formula: H=(c1*​a**(k−1))+(c2*​a**(k−2))+c3​ak−3+⋯+ck​a0
https://brilliant.org/wiki/rabin-karp-algorithm/
"""
class RollingHash:
    def __init__(self, text, size):
        self.text = text
        self.size = size
        self.hash = 0
        self.window_start = 0
        self.window_end = size

        for i in range(size):
            self.hash += (ord(self.text[i]) - ord("a") + 1) * (26 ** (size - i - 1))

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            # remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a") + 1) * 26 ** (self.sizeWord - 1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a") + 1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]


def rabin_karp(word, text):
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    #word_hash.move_window()

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return None
