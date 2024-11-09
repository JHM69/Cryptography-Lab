from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode()

# Example
text = "JAHANGIR IS BEST"
key = b'8bytekey'
encrypted = des_encrypt(text, key)
decrypted = des_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")