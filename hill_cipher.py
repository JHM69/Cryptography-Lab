import numpy as np

def hill_encrypt(text, key_matrix):
    n = len(key_matrix)
    text = text.upper().replace(" ", "")
    while len(text) % n != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), n):
        block = [ord(char) - ord('A') for char in text[i:i+n]]
        encrypted_block = np.dot(key_matrix, block) % 26
        result += ''.join(chr(num + ord('A')) for num in encrypted_block)
    return result

def hill_decrypt(text, key_matrix):
    n = len(key_matrix)
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = pow(det, -1, 26)
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_key_matrix = (det_inv * adjugate) % 26
    result = ""
    for i in range(0, len(text), n):
        block = [ord(char) - ord('A') for char in text[i:i+n]]
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        result += ''.join(chr(num + ord('A')) for num in decrypted_block)
    return result

# Example
text = "JAHANGIR IS BEST"
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
encrypted = hill_encrypt(text, key_matrix)
decrypted = hill_decrypt(encrypted, key_matrix)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")