import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    priority_queue = []
    for char, freq in frequency.items():
        heapq.heappush(priority_queue, Node(char, freq))
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(priority_queue, internal_node)
    return priority_queue[0]

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return codes
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

def encode(data, codes):
    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data

def decode(encoded_data, root):
    decoded_data = []
    node = root
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_data.append(node.char)
            node = root
    return ''.join(decoded_data)

if __name__ == "__main__":
    data = "this is an example for huffman encoding"
    frequency = calculate_frequency(data)
    root = build_huffman_tree(frequency)
    huffman_codes = generate_codes(root)
    encoded_data = encode(data, huffman_codes)
    print(f"Encoded data: {encoded_data}")
    decoded_data = decode(encoded_data, root)
    print(f"Decoded data: {decoded_data}")
