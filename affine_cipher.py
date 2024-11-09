def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            num = ord(char) - ord('A')
            encrypted_num = (a * num + b) % 26
            result += chr(encrypted_num + ord('A'))
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    inverse_a = mod_inverse(a, 26)
    if inverse_a is None:
        raise ValueError("No modular inverse exists for the given key.")
    
    result = ""
    for char in text:
        if char.isalpha():
            num = ord(char) - ord('A')
            decrypted_num = (inverse_a * (num - b)) % 26
            result += chr(decrypted_num + ord('A'))
        else:
            result += char
    return result

# Example
text = "JAHANGIR IS BEST"
a, b = 5, 8
encrypted = affine_encrypt(text, a, b)
decrypted = affine_decrypt(encrypted, a, b)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")