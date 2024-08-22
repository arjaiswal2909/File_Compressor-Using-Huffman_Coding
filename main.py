from huffman.encoder import compress_file
from huffman.decoder import decompress_file

def main():
    input_file = input("Enter the name of the input file: ")
    compressed_file = input("Enter the name of the compressed file: ")
    decompressed_file = input("Enter the name of the decompressed file: ")

    # Compress the file
    huffman_codes = compress_file(input_file, compressed_file)
    print(f"File '{input_file}' has been compressed to '{compressed_file}'.")

    # Decompress the file
    decompress_file(compressed_file, decompressed_file, huffman_codes)
    print(f"File '{compressed_file}' has been decompressed to '{decompressed_file}'.")

if __name__ == "__main__":
    main()
