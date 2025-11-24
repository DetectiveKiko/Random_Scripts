

def encrypt(plaintext, shift_key):

    ciphertext = ""

    for char in plaintext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_shifted = (char_index + shift_key) % 26 + ord("A")
            char_encrypted = chr(char_shifted)
            ciphertext += char_encrypted

        elif char.islower():
            char_index = ord(char) - ord("a")
            char_shifted = (char_index + shift_key) % 26 + ord("a")
            char_encrypted = chr(char_shifted)
            ciphertext += char_encrypted

        else:
            ciphertext += char

    return ciphertext

def decrypt (ciphertext, shift_key):

    decrypt_plaintext = ""

    for char in ciphertext:
        if char.isupper():

            char_index = ord(char) - ord("A")
            char_unshifted = (char_index - shift_key) % 26 + ord("A")
            char_decrypt = chr(char_unshifted)
            decrypt_plaintext += char_decrypt

        elif char.islower():
            char_index = ord(char) - ord("a")
            char_unshifted = (char_index - shift_key) % 26 + ord("a")
            char_decrypt = chr(char_unshifted)
            decrypt_plaintext += char_decrypt

        else:
            decrypt_plaintext += char

    return decrypt_plaintext

plaintext = input("Enter PlainText: ")
shift_key = int(input("Enter shift key: "))
shift_amount = 26 - shift_key
ciphertext = encrypt(plaintext, shift_key)
decrypted_plaintext = decrypt(ciphertext, shift_key)

print("PlainText: " + plaintext)
print("Character Shift: " + str(shift_key))
print("Encrypted PlainText: " + ciphertext)
print("Decrypted PlainText: " + decrypted_plaintext)
