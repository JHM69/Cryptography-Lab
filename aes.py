from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
    return decrypted_text.decode()

# Example
text = "JAHANGIR IS BEST"
key = b'16bytekey1234567'  
encrypted = aes_encrypt(text, key)
decrypted = aes_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")