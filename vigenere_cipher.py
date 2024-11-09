def vigenere_encrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = (ord(char.upper()) + shift - ord('A')) % 26 + ord('A')
            result += chr(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = (ord(char) - shift - ord('A')) % 26 + ord('A')
            result += chr(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

# Example
text = "JAHANGIR IS BEST"
key = "KEY"
encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")