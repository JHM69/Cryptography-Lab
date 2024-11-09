def multiplicative_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            num = ord(char) - ord('A')
            encrypted_num = (num * key) % 26
            result += chr(encrypted_num + ord('A'))
        else:
            result += char
    return result

def multiplicative_decrypt(text, key):
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    inverse_key = mod_inverse(key, 26)
    if inverse_key is None:
        raise ValueError("No modular inverse exists for the given key.")
    
    result = ""
    for char in text:
        if char.isalpha():
            num = ord(char) - ord('A')
            decrypted_num = (num * inverse_key) % 26
            result += chr(decrypted_num + ord('A'))
        else:
            result += char
    return result

# Example
text = "JAHANGIR IS BEST"
key = 3
encrypted = multiplicative_encrypt(text, key)
decrypted = multiplicative_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")