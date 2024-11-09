def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example
text = "JAHANGIR IS BEST"
shift = 3
encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")