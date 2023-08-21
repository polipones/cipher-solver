import sys


def main():
    # Check for right number of arguments
    if len(sys.argv) != 3:
        print('Wrong number of arguments.')
        print_usage()
        exit(1)

    # Read key file
    key = read_file(sys.argv[1])

    if len(key) != 2:
        print(
            'File with key should contain exactly two lines, where first line is plaintext alphabet and second one is '
            'mapping to cipher')
        print_usage()
        exit(2)

    # Format key into map
    key_map = make_key_map(key)

    # Read ciphertext file
    ciphertext = read_file(sys.argv[2])

    print('Decrypted text is:')

    # Decode line one by one and print result to stdout
    for line in ciphertext:
        print(decrypt_line(key_map, line))


def decrypt_line(key_map: dict[str, str], ciphertext: str) -> str:
    plaintext = ''

    for letter in ciphertext:
        if letter not in key_map:
            print('There is no plain letter for cipher letter {}'.format(letter))
            exit(3)

        plaintext += key_map[letter]

    return plaintext


def print_usage():
    print('Usage:')
    print('{} <filename with key> <filename with ciphertext>'.format(sys.argv[0]))


def read_file(filename: str) -> list[str]:
    try:
        # Read file
        with open(filename, 'r') as file:
            file_contents = file.readlines()

        # Strip extra newlines
        file_contents = [l.strip() for l in file_contents]

        return file_contents
    except FileNotFoundError:
        print('Error: The file {} was not found.'.format(filename))
    except PermissionError:
        print('Error: You don\'t have permission to access the file {}.'.format(filename))
    except Exception as e:
        print('An error occurred: '.format(e))


def make_key_map(raw_key: list[str]) -> dict[str, str]:
    km: dict = {}

    plain_alphabet = raw_key[0]
    cipher_alphabet = raw_key[1]

    if len(plain_alphabet) != len(cipher_alphabet):
        print(
            'Lengths of plain and cipher alphabet are not the same! {} vs. {}'
            .format(len(plain_alphabet), len(cipher_alphabet))
        )
        exit(2)

    for index, cipher_word in enumerate(cipher_alphabet):
        km[cipher_word] = plain_alphabet[index]

    return km


main()
