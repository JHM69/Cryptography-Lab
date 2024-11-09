import random

def one_time_pad_encrypt(text, key):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            encrypted_char = (ord(char.upper()) + shift - ord('A')) % 26 + ord('A')
            result += chr(encrypted_char)
        else:
            result += char
    return result

def one_time_pad_decrypt(text, key):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            decrypted_char = (ord(char) - shift - ord('A')) % 26 + ord('A')
            result += chr(decrypted_char)
        else:
            result += char
    return result

# Example
text = "JAHANGIR IS BEST"
key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(text)))
encrypted = one_time_pad_encrypt(text, key)
decrypted = one_time_pad_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")