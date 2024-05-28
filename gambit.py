from string import ascii_letters
import re

def load_cipher_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return [int(number) for number in re.findall(r'\d+', content)]

def is_valid_decryption(decrypted_text, valid_chars):
    return all(char in valid_chars for char in decrypted_text)

def find_shifts_for_offsets(cipher_numbers, valid_chars):
    shift_map = {}
    for offset in range(3):
        for shift in range(256):
            decrypted = [(chr((num - shift) % 256)) for num in cipher_numbers[offset::3]]
            if is_valid_decryption(decrypted, valid_chars):
                shift_map[offset] = shift
                break
    return shift_map

def decrypt_message(cipher_numbers, shift_map):
    return ''.join([chr((num - shift_map[i % 3]) % 256) for i, num in enumerate(cipher_numbers)])

def main():
    valid_characters = ascii_letters + " .,@:" + "0123456789"
    file_path = 'cipher.txt'
    cipher_numbers = load_cipher_from_file(file_path)
    shift_map = find_shifts_for_offsets(cipher_numbers, valid_characters)
    decrypted_message = decrypt_message(cipher_numbers, shift_map)
    print(f"a: {shift_map.get(0, 'Not found')}, b: {shift_map.get(1, 'Not found')}, c: {shift_map.get(2, 'Not found')}")
    print(decrypted_message)


if __name__ == "__main__":
    main()
