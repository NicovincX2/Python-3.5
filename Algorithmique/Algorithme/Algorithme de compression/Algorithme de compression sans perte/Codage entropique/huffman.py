# -*- coding: utf-8 -*-

import os
import numpy

def char_count(text):
    histogram = {}
    for ch in text:
        histogram[ch] = histogram.get(ch, 0) + 1
    return histogram

letter_count = char_count("live and let live")
letter_count

def by_value(tup):
    return tup[1]

def build_huffman_tree(letter_count):
    """ recieves dictionary with char:count entries
        generates a list of letters representing the binary Huffman encoding tree"""
    queue = list(letter_count.items())
    while len(queue) >= 2:
        queue.sort(key=by_value)  # sort by the count
        # combine two least frequent elements
        elem1, freq1 = queue.pop(0)
        elem2, freq2 = queue.pop(0)
        elems = (elem1, elem2)
        freqs = freq1 + freq2
        queue.append((elems,freqs))
    return queue[0][0]

tree = build_huffman_tree(letter_count)
tree

def build_codebook(huff_tree, prefix=''):
    """ receives a Huffman tree with embedded encoding and a prefix of encodings.
        returns a dictionary where characters are keys and associated binary strings are values."""
    if isinstance(huff_tree, str): # a leaf
        return {huff_tree: prefix}
    else:
        left, right = huff_tree
        codebook = {}
        codebook.update( build_codebook(left,  prefix + '0'))
        codebook.update( build_codebook(right, prefix + '1'))
        return codebook

codebook = build_codebook(tree)
for ch,freq in sorted(letter_count.items(), key=by_value, reverse=True):
    print(ch, freq, codebook[ch])

def compress(text, codebook):
  ''' compress text using codebook dictionary '''
  return ''.join(codebook[ch] for ch in text if ord(ch) <= 128)

ch,ord(ch),'{:08b}'.format(ord(ch))

bits_ascii = ''.join(['{:07b}'.format(ord(ch)) for ch in "live and let live" if ord(ch) <= 128])
huff_bits = compress("live and let live", codebook)

print(len(bits_ascii),bits_ascii)
print(len(huff_bits),huff_bits)

def build_decoding_dict(codebook):
   """build the "reverse" of encoding dictionary"""
   return {v:k for k,v in codebook.items()}

decodebook = build_decoding_dict(codebook)
decodebook

def decompress(bits, decodebook):
   prefix = ''
   result = []
   for bit in bits:
      prefix += bit
      if prefix not in decodebook:
         continue
      result.append(decodebook[prefix])
      prefix = ''
   assert prefix == '' # must finish last codeword
   return ''.join(result)  # converts list of chars to a string

decompress(huff_bits, decodebook)

def huffman_code(corpus):
    counts = char_count(corpus)
    tree = build_huffman_tree(counts)
    return build_codebook(tree)

huffman_code('aaabbc')
huffman_code('aaabbcc')
codebook = huffman_code('qwertuioplkjhgfdsazxcvbnm')
codebook

mean([len(v) for v in codebook.values()])

corpus = ''.join([ch*(i+1) for i,ch in enumerate('qwertuioplkjhgfdsazxcvbnm') ])
corpus

huffman_code(corpus)
print(''.join([chr(c) for c in range(128)]))

def compression_ratio(text, corpus):
    codebook = huffman_code(corpus)
    len_compress = len(compress(text, codebook))
    len_ascii = len(text) * 7
    return len_compress / len_ascii

from urllib.request import urlopen

with urlopen("http://www.gutenberg.org/cache/epub/42745/pg42745.txt") as f:
    gauss = f.read().decode('utf-8')
print(gauss[:gauss.index('\n\r')])

with urlopen("http://www.gutenberg.org/files/25447/25447-0.txt") as f:
    russell = f.read().decode('utf-8')
print(russell[:russell.index('\n\r')])

with urlopen("http://www.gutenberg.org/files/42743/42743-0.txt") as f:
    table_ronde = f.read().decode('utf-8')
print(table_ronde[:table_ronde.index('\n\r')])

with urlopen("http://www.gutenberg.org/cache/epub/97/pg97.txt") as f:
    flatland_book = f.read().decode('utf-8')
print(flatland_book[:flatland_book.index('\n\r')])

print("self",compression_ratio(flatland_book, flatland_book))
print("en",compression_ratio(flatland_book, russell))
print("de",compression_ratio(flatland_book, gauss))
print("fr",compression_ratio(flatland_book, table_ronde))

import pydot # https://github.com/nlhepler/pydot-py3, http://pyparsing.wikispaces.com/Download+and+Installation

def tree_to_str(tree):
    if isinstance(tree, str):
        return tree
    return ''.join([tree_to_str(item) for item in tree])

def add_to_node(tree, node, graph):
    left, right = tree
    left_node, right_node = pydot.Node(tree_to_str(left)), pydot.Node(tree_to_str(right))
    graph.add_node(left_node)
    graph.add_node(right_node)
    graph.add_edge(pydot.Edge(node, left_node))
    graph.add_edge(pydot.Edge(node, right_node))
    if not isinstance(left, str):
        add_to_node(left, left_node, graph)
    if  not isinstance(right, str):
        add_to_node(right, right_node, graph)

def tree_to_graph(tree):
    graph = pydot.Dot(graph_type='digraph',strict=True)
    root = pydot.Node(tree_to_str(tree))
    graph.add_node(root)
    add_to_node(tree, root, graph)
    return graph

tree_to_str(tree)

graph = tree_to_graph(tree)

with open("tmp.dot","w") as f:
    f.write(graph.to_string())
# !dot tmp.dot -Tpng -ohuffman_tree.png
# !huffman_tree.png

for c in flatland_book:
    if ord(c) >= 128:
        print(ord(c))

flatland_book_clean = flatland_book.replace(chr(65279), '').replace('"','').replace("'",'').replace(",",'').replace(";",'').replace(":",'').replace(".",'')
flatland_tree = build_huffman_tree(char_count(flatland_book_clean.lower()))
tree_to_str(flatland_tree)

graph = tree_to_graph(flatland_tree)

with open("tmp.dot","w") as f:
    f.write(graph.to_string())
# !dot tmp.dot -Tpng -oflatland_tree.png
# !flatland_tree.png

os.system("pause")
