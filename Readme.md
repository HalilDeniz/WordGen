# WordGen

WordGen is a powerful wordlist generator tool that allows you to generate custom wordlists for various purposes, such as password cracking, security assessments, and more.

## Features

- Generate wordlists based on specified character set, minimum and maximum word lengths.
- Filter wordlists based on patterns to meet specific requirements.
- Save wordlists to output files.
- Compress wordlists into zip files.
- Exclude specific characters or character sets from the generated wordlists.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/HalilDeniz/WordGen.git
   ```

2. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```
## fist See
   ```
root@denizhalil:/myProject/WordGen# python3 wordgen.py --help
usage: wordgen.py [-h] [-p PATTERN] [-o OUTPUT] [-z] [-f FILE] [-e EXCLUDE] min_length max_length charset

Crunch Wordlist Generator

positional arguments:
  min_length            Minimum length of generated words
  max_length            Maximum length of generated words
  charset               Character set to use for generating the wordlist

options:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        Pattern to filter wordlist generation
  -o OUTPUT, --output OUTPUT
                        Output file name
  -z, --compress        Compress wordlist into a zip file
  -f FILE, --file FILE  Input file name
  -e EXCLUDE, --exclude EXCLUDE
                        Characters to exclude from the wordlist
```

## Usage

```shell
python wordgen.py <min_length> <max_length> <charset> [options]
```

- `<min_length>`: Minimum length of generated words.
- `<max_length>`: Maximum length of generated words.
- `<charset>`: Character set to use for generating the wordlist.

### Options

- `-p, --pattern`: Pattern to filter wordlist generation.
- `-o, --output`: Output file name.
- `-z, --compress`: Compress wordlist into a zip file.
- `-f, --file`: Input file name to include additional words.
- `-e, --exclude`: Characters to exclude from the wordlist.

## Example
```
root@denizhalil:~/myProject/WordGen# python3 wordgen.py 6 6 1234567890 -o test.txt
Wordlist generated successfully and saved to 'test.txt'.
Total words generated: 1000000
Total time taken: 0.32 seconds
Total size: 39000000 bytes
```

## Contributing
Contributions are welcome! To contribute to WordGen, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in the main repository.

## Contact

- LinkedIn: [Halil Ibrahim Deniz](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe: [Halil Deniz](https://tryhackme.com/p/halilovic)
- Instagram: [@deniz.halil333](https://www.instagram.com/deniz.halil333/)
- YouTube: [Halil Deniz](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
