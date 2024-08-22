def decompress_file(input_file, output_file, huffman_codes):
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}

    with open(input_file, 'rb') as file:
        encoded_text = file.read().decode('utf-8')

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_text += reverse_huffman_codes[current_code]
            current_code = ""

    with open(output_file, 'w') as file:
        file.write(decoded_text)
