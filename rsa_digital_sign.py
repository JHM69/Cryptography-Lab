from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def rsa_sign(text, private_key):
    h = SHA256.new(text.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def rsa_verify(text, signature, public_key):
    h = SHA256.new(text.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Example
key = RSA.generate(2048)
public_key = key.publickey()
text = "JAHANGIR IS BEST"
signature = rsa_sign(text, key)
is_verified = rsa_verify(text, signature, public_key)
print(f"Signature: {signature}, Verified: {is_verified}")