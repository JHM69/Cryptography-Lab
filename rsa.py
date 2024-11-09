from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(text, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

def rsa_decrypt(encrypted_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode()

# Example
key = RSA.generate(2048)
public_key = key.publickey()
text = "JAHANGIR IS BEST"
encrypted = rsa_encrypt(text, public_key)
decrypted = rsa_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")