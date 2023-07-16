import heapq
import math

# Node class for Huffman tree
class Node:
    def __init__(self, probability, symbol=None):
        self.probability = probability
        self.symbol = symbol
        self.left = None
        self.right = None

    # Define comparison operators for heapq
    def __lt__(self, other):
        return self.probability < other.probability

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.probability == other.probability
        return False

# Function to build Huffman tree
def build_huffman_tree(probabilities):
    # Create a priority queue (min-heap)
    pq = []
    for symbol, probability in enumerate(probabilities):
        node = Node(probability, symbol)
        heapq.heappush(pq, node)

    # Build Huffman tree
    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        merged_prob = node1.probability + node2.probability
        merged_node = Node(merged_prob)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(pq, merged_node)

    return pq[0]

#codeword
def generate_c(node, code='', c={}):
    if node.symbol is not None:
        c[node.symbol] = code
    else:
        generate_c(node.left, code + '0', c)
        generate_c(node.right, code + '1', c)
    return c

#calculations
def calculate_al(probabilities, c):
    Li = 0.0
    for symbol, probability in enumerate(probabilities):
        codeword = c[symbol]
        Li += probability * len(codeword)
    return Li

def calculate_H(probabilities):
    H = 0.0
    for probability in probabilities:
        if probability > 0:
            H -= probability * math.log2(probability)
    return H

def calculate_n(H, Li):
    return (H / Li)*100

def calculate_r(H, Li):
    return (1-(H / Li))*100

def calculate_v(probabilities, c, Li):
    v = 0.0
    for symbol, probability in enumerate(probabilities):
        codeword = c[symbol]
        v += probability * ((len(codeword) - Li) ** 2)
    return v

#Taking Input
probabilities=[]
n=int(input("enter No of Probabilities: "))
for i in range(0,n):
    ele = float(input(f"enter probability No. {i+1}: "))
    probabilities.append(ele)
    
#Function Calling
huffman_tree = build_huffman_tree(probabilities)
c = generate_c(huffman_tree)
Li = calculate_al(probabilities, c)
H = calculate_H(probabilities)
n = calculate_n(H, Li)
r = calculate_r(H, Li)
v = calculate_v(probabilities, c, Li)

#Output
print()
print('Codewords (C) :', c  )
print('Average Length (Li) :', Li,"Bits per Symbol")
print('Entropy (H) :', H, "Bits per Symbol" )
print('Efficiency (n) :', n,"Percent Efficient")
print('Redundancy (1-n) :', r)
print('Variance (σ2) :', v)