def autokey_encrypt(text, key):
    key = (key.upper() + text.upper()).replace(" ", "")  # Extend key and remove spaces
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            encrypted_char = (ord(char.upper()) + shift - ord('A')) % 26 + ord('A')
            result += chr(encrypted_char)
        else:
            result += char
    return result

def autokey_decrypt(text, key):
    key = key.upper()
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i]) - ord('A')
            decrypted_char = (ord(char) - shift - ord('A')) % 26 + ord('A')
            result += chr(decrypted_char)
            key += chr(decrypted_char)  # Extend key with decrypted char for autokey
        else:
            result += char
    return result

# Example
text = "JAHANGIR IS BEST"
key = "KEY"
encrypted = autokey_encrypt(text, key)
decrypted = autokey_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")
