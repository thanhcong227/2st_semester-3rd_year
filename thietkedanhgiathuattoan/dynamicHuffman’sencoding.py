import heapq
from collections import defaultdict

# Node class to represent a symbol and its frequency in the data
class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# Dynamic Huffman coding class
class DynamicHuffman:
    def __init__(self):
        self.root = None
        self.codes = defaultdict(str)
        self.heap = []

    # Update the tree with a new symbol and its frequency
    def update_tree(self, symbol):
        # If the symbol is not already in the tree, add it with a frequency of 1
        if symbol not in self.codes:
            self.codes[symbol] = "1"
            node = Node(symbol, 1)
            heapq.heappush(self.heap, node)
        # If the symbol is already in the tree, update its frequency and reorganize the tree
        else:
            self.codes[symbol] = self.codes[symbol][:-1] + "1"
            node = self.get_node(symbol)
            node.frequency += 1
            heapq.heapify(self.heap)

            # Reorganize the tree if necessary
            while node != self.heap[0]:
                parent = self.get_parent(node)
                if node.frequency < parent.frequency:
                    node, parent = parent, node
                parent.left, parent.right = node, parent.left
                node = parent

    # Get the node corresponding to a symbol
    def get_node(self, symbol):
        for node in self.heap:
            if node.symbol == symbol:
                return node

    # Get the parent node of a given node
    def get_parent(self, node):
        for parent in self.heap:
            if parent.left == node or parent.right == node:
                return parent

    # Generate the codes for each symbol based on the Huffman tree
    def generate_codes(self, node, code):
        if node is None:
            return
        if node.symbol:
            self.codes[node.symbol] = code
        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    # Encode a string using the Huffman codes
    def encode(self, data):
        encoded_data = ""
        for symbol in data:
            encoded_data += self.codes[symbol]
            self.update_tree(symbol)
        return encoded_data


