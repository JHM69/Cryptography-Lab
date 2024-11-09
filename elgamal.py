from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Util.number import GCD

def elgamal_encrypt(text, key):
    cipher = ElGamal.construct(key)
    k = get_random_bytes(16)
    while GCD(k, key.p - 1) != 1:
        k = get_random_bytes(16)
    encrypted_text = cipher.encrypt(text.encode(), k)
    return encrypted_text

def elgamal_decrypt(encrypted_text, key):
    cipher = ElGamal.construct(key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode()

# Example
key = ElGamal.generate(256, get_random_bytes)
text = "JAHANGIR IS BEST"
encrypted = elgamal_encrypt(text, key)
decrypted = elgamal_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")