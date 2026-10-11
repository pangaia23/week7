def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print('|   ', end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i % alpha_len]}", end=' ')
    print('|')
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i + shift) % alpha_len]
                print(f"| {c}", end=' ')
                print(f"| {c}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")
def letter_to_index(letter, alphabet: str):
    return alphabet.lower().index(letter.lower())


def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''
def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif(c.upper() in alphabet):
            cipher_text += index_to_letter(vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    return (letter_to_index(cypher_letter, alphabet) -
            letter_to_index(key_letter, alphabet)) % len(alphabet)


def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ''
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plain_text += ' '
        elif c.upper() in alphabet:
            plain_text += index_to_letter(undo_vigenere_index(key[counter % len(key)], c, alphabet), alphabet)
            counter += 1
    return plain_text

def menu():
    print('1). Encrypt or 2). Decrypt')
    choice = input('Select an option: ')

    if choice == '1':
        key = input('Enter key: ')
        text = input('Enter plain text: ')
        print(encrypt_vigenere(key, text, alphabet))
        menu()
    elif choice == '2':
        key = input('Enter key: ')
        text = input('Enter cipher text: ')
        print(decrypt_vigenere(key, text, alphabet))



alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# vigenere_sq(alphabet)
# print(letter_to_index('H', alphabet))
# print(index_to_letter(7, alphabet))
# print(
#     index_to_letter(
#         vigenere_index('B', 'H', alphabet), alphabet)
# )

#encrypted = encrypt_vigenere(key, message, alphabet)
#print(f"Encrypted: {encrypted}")

#decrypted = decrypt_vigenere(key, encrypted, alphabet)
#print(f"Decrypted: {decrypted}")

menu()