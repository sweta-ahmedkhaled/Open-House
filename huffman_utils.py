class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
