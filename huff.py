import heapq

from huffman_utils import Node
from huffman_build import build_tree
from huffman_codes import get_codes


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
