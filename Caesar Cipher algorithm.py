def caesar_encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        # Encrypt only alphabetic characters
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                cipher_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            # Handle lowercase letters
            elif char.islower():
                cipher_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            # Keep non-alphabet characters as they are
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        # Decrypt only alphabetic characters
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                plain_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            # Handle lowercase letters
            elif char.islower():
                plain_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            # Keep non-alphabet characters as they are
            plain_text += char
    return plain_text

# Get user input
plain_text = input("Enter Plain Text: ")
print("Plain Text:", plain_text)

# Set Caesar Cipher key
key = 3

# Encrypt the plain text
cipher_text = caesar_encrypt(plain_text, key)
print("Cipher Text:", cipher_text)

# Decrypt the cipher text
decrypted_text = caesar_decrypt(cipher_text, key)
print("Decrypted Plain Text:", decrypted_text)
