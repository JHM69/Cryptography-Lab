def knapsack_encrypt(text, public_key):
    encrypted_text = []
    for char in text:
        bits = bin(ord(char))[2:].zfill(8)
        encrypted_char = sum(int(bit) * pk for bit, pk in zip(bits, public_key))
        encrypted_text.append(encrypted_char)
    return encrypted_text

def knapsack_decrypt(encrypted_text, private_key, modulus, multiplier):
    decrypted_text = ""
    inverse_multiplier = pow(multiplier, -1, modulus)
    for encrypted_char in encrypted_text:
        c = (encrypted_char * inverse_multiplier) % modulus
        bits = []
        for pk in reversed(private_key):
            if pk <= c:
                bits.append(1)
                c -= pk
            else:
                bits.append(0)
        bits.reverse()
        char = chr(int("".join(map(str, bits)), 2))
        decrypted_text += char
    return decrypted_text

# Example
private_key = [2, 3, 6, 13, 27, 52, 105, 210]
modulus = 420
multiplier = 31
public_key = [(multiplier * pk) % modulus for pk in private_key]
text = "JAHANGIR IS BEST"
encrypted = knapsack_encrypt(text, public_key)
decrypted = knapsack_decrypt(encrypted, private_key, modulus, multiplier)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")