import argparse
import itertools
import time
import sys
import multiprocessing
import zipfile

def generate_wordlist(charset, min_length, max_length, pattern=None, input_file=None, exclude_chars=None):
    start_time = time.time()
    wordlist = []
    total_count = 0
    total_size = 0

    # Giriş dosyası belirtilmişse, dosyadaki kelimeleri oku
    if input_file:
        with open(input_file, 'r') as file:
            wordlist.extend(line.strip() for line in file)

    if pattern:
        combinations = itertools.product(charset, repeat=len(pattern))
        pattern = ''.join(pattern)
        combinations = [combo for combo in combinations if ''.join(combo).startswith(pattern)]
    else:
        combinations = itertools.product(charset, repeat=max_length)

    for combination in combinations:
        word = ''.join(combination)
        if exclude_chars and any(char in word for char in exclude_chars):
            continue  # Hariç tutulan karakterler içeren kelimeleri atla
        wordlist.append(word)
        total_count += 1
        total_size += sys.getsizeof(word.encode())

    end_time = time.time()
    total_time = end_time - start_time
    return wordlist, total_count, total_time, total_size

def save_wordlist(wordlist, output_file):
    with open(output_file, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

def compress_wordlist(wordlist, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i, word in enumerate(wordlist, 1):
            zipf.writestr(f'wordlist_{i}.txt', word)

def main():
    parser = argparse.ArgumentParser(description='Crunch Wordlist Generator')
    parser.add_argument('min_length', type=int, help='Minimum length of generated words')
    parser.add_argument('max_length', type=int, help='Maximum length of generated words')
    parser.add_argument('charset', type=str, help='Character set to use for generating the wordlist')
    parser.add_argument('-p', '--pattern', type=str, help='Pattern to filter wordlist generation')
    parser.add_argument('-o', '--output', type=str, help='Output file name')
    parser.add_argument('-z', '--compress', action='store_true', help='Compress wordlist into a zip file')
    parser.add_argument('-f', '--file', type=str, help='Input file name')
    parser.add_argument('-e', '--exclude', type=str, help='Characters to exclude from the wordlist')

    args = parser.parse_args()

    charset = args.charset
    min_length = args.min_length
    max_length = args.max_length
    pattern = args.pattern
    output_file = args.output
    compress = args.compress
    input_file = args.file
    exclude_chars = args.exclude

    wordlist, total_count, total_time, total_size = generate_wordlist(charset, min_length, max_length, pattern, input_file, exclude_chars)

    if output_file:
        if compress:
            output_file += '.zip'
            compress_wordlist(wordlist, output_file)
        else:
            save_wordlist(wordlist, output_file)
        print(f"Wordlist generated successfully and saved to '{output_file}'.")
    else:
        for word in wordlist:
            print(word)

    print(f"Total words generated: {total_count}")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Total size: {total_size} bytes")


if __name__ == "__main__":
	main()

