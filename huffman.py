import heapq

# ── Huffman Node ───────────────────────────────────────────────────────────────
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ── Build Tree ─────────────────────────────────────────────────────────────────
def build_tree(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left  = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(heap, parent)

    return heapq.heappop(heap)


# ── Generate Codes ─────────────────────────────────────────────────────────────
def get_codes(node, prefix="", codes={}):
    if node.char is not None:
        codes[node.char] = prefix
    else:
        get_codes(node.left,  prefix + "0", codes)
        get_codes(node.right, prefix + "1", codes)
    return codes


# ── Demo ───────────────────────────────────────────────────────────────────────
text = "dogs do good deeds"

tree  = build_tree(text)
codes = get_codes(tree, "", {})

original_bits  = len(text) * 8
compressed_bits = sum(len(codes[ch]) for ch in text)

print(f"Text : '{text}'")
print()
print(f"{'Char':<6} {'Freq':<6} {'Code':<10} {'Bits saved'}")
print("-" * 38)
for ch, code in sorted(codes.items(), key=lambda x: len(x[1])):
    label = repr(ch)
    print(f"{label:<6} {text.count(ch):<6} {code:<10} {8 - len(code)} bits each")

print()
print(f"Original   : {original_bits} bits  ({len(text)} chars × 8 bits)")
print(f"Compressed : {compressed_bits} bits")
print(f"Saved      : {original_bits - compressed_bits} bits  →  {(1 - compressed_bits/original_bits)*100:.1f}% smaller")
import heapq

# ── Huffman Node ───────────────────────────────────────────────────────────────
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ── Build Tree ─────────────────────────────────────────────────────────────────
def build_tree(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left  = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(heap, parent)

    return heapq.heappop(heap)


# ── Generate Codes ─────────────────────────────────────────────────────────────
def get_codes(node, prefix="", codes={}):
    if node.char is not None:
        codes[node.char] = prefix
    else:
        get_codes(node.left,  prefix + "0", codes)
        get_codes(node.right, prefix + "1", codes)
    return codes


# ── Demo ───────────────────────────────────────────────────────────────────────
text = "dogs do good deeds"

tree  = build_tree(text)
codes = get_codes(tree, "", {})

original_bits  = len(text) * 8
compressed_bits = sum(len(codes[ch]) for ch in text)

print(f"Text : '{text}'")
print()
print(f"{'Char':<6} {'Freq':<6} {'Code':<10} {'Bits saved'}")
print("-" * 38)
for ch, code in sorted(codes.items(), key=lambda x: len(x[1])):
    label = repr(ch)
    print(f"{label:<6} {text.count(ch):<6} {code:<10} {8 - len(code)} bits each")

print()
print(f"Original   : {original_bits} bits  ({len(text)} chars × 8 bits)")
print(f"Compressed : {compressed_bits} bits")
print(f"Saved      : {original_bits - compressed_bits} bits  →  {(1 - compressed_bits/original_bits)*100:.1f}% smaller")