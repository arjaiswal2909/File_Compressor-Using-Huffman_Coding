from huffman_tree import build_huffman_tree, generate_huffman_codes

def compress_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    chars = list(frequency.keys())
    freq = list(frequency.values())

    root = build_huffman_tree(chars, freq)
    huffman_codes = generate_huffman_codes(root)

    encoded_text = ''.join([huffman_codes[char] for char in text])

    with open(output_file, 'wb') as file:
        file.write(encoded_text.encode('utf-8'))

    return huffman_codes
