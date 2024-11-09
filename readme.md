# Cryptography Algorithms

This project has some cryptographic algorithms, including traditional ciphers, polyalphabetic ciphers, modern block ciphers, and digital signatures. Each section includes the mathematical foundation and a brief explanation of the algorithm.

## Traditional Ciphers (Monoalphabetic)

### Caesar Cipher

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

**Mathematical Representation:**

For a given plaintext letter \( P \) and a shift \( k \), the ciphertext letter \( C \) is given by:

$$ C = (P + k) \mod 26 $$

**Decryption:**

$$ P = (C - k) \mod 26 $$

### Multiplicative Cipher

The Multiplicative Cipher uses multiplication to encrypt the message.

**Mathematical Representation:**

For a given plaintext letter \( P \) and a key \( k \), the ciphertext letter \( C \) is:

$$ C = (P \times k) \mod 26 $$

**Decryption:**

To decrypt, we need the modular inverse \( k^{-1} \) of \( k \):

$$ P = (C \times k^{-1}) \mod 26 $$

### Affine Cipher

The Affine Cipher combines both multiplicative and additive ciphers.

**Mathematical Representation:**

For a given plaintext letter \( P \), the ciphertext letter \( C \) is:

$$ C = (a \times P + b) \mod 26 $$

**Decryption:**

$$ P = a^{-1} \times (C - b) \mod 26 $$

where \( a^{-1} \) is the modular inverse of \( a \).

## Polyalphabetic Ciphers

### Autokey Cipher

The Autokey Cipher uses a keyword and the plaintext to generate the keystream.

**Encryption:**

For a given plaintext \( P \) and key \( K \):

$$ C_i = (P_i + K_i) \mod 26 $$

**Decryption:**

$$ P_i = (C_i - K_i) \mod 26 $$

### Playfair Cipher

The Playfair Cipher uses a 5x5 matrix to encrypt pairs of letters.

**Encryption:**

- If both letters are in the same row, replace them with the letters to their immediate right.
- If both letters are in the same column, replace them with the letters immediately below.
- Otherwise, replace them with the letters on the same row but at the opposite corners of the rectangle.

### Vigenère Cipher

The Vigenère Cipher uses a keyword to shift letters.

**Mathematical Representation:**

For a given plaintext \( P \) and key \( K \):

$$ C_i = (P_i + K_i) \mod 26 $$

**Decryption:**

$$ P_i = (C_i - K_i) \mod 26 $$

### Hill Cipher

The Hill Cipher uses linear algebra to encrypt blocks of text.

**Mathematical Representation:**

For a block of plaintext represented as a vector \( \mathbf{P} \) and a key matrix \( \mathbf{K} \):

$$ \mathbf{C} = \mathbf{K} \cdot \mathbf{P} \mod 26 $$

**Decryption:**

$$ \mathbf{P} = \mathbf{K}^{-1} \cdot \mathbf{C} \mod 26 $$

where \( \mathbf{K}^{-1} \) is the inverse of the key matrix.

### One Time Pad

The One Time Pad uses a random key that is as long as the message.

**Encryption:**

$$ C_i = (P_i + K_i) \mod 26 $$

**Decryption:**

$$ P_i = (C_i - K_i) \mod 26 $$

### Rail Fence Cipher

The Rail Fence Cipher writes the message in a zigzag pattern.

**Encryption:**

The message is written in a zigzag pattern across multiple "rails" and then read off row by row.

## Modern Block Ciphers

### DES (Data Encryption Standard)

DES is a symmetric-key algorithm that uses a 56-bit key to encrypt data in 64-bit blocks.

**Mathematical Representation:**

DES uses a series of permutations and substitutions based on the key to transform the plaintext into ciphertext.

### AES (Advanced Encryption Standard)

AES is a symmetric encryption algorithm that encrypts data in 128-bit blocks using keys of 128, 192, or 256 bits.

**Mathematical Representation:**

AES uses a series of transformations including substitution, permutation, and mixing of the input data.

### ElGamal

ElGamal is an asymmetric key encryption algorithm based on the Diffie-Hellman key exchange.

**Mathematical Representation:**

- **Encryption:** \( C_1 = g^k \mod p \), \( C_2 = M \times y^k \mod p \)
- **Decryption:** \( M = C_2 \times (C_1^x)^{-1} \mod p \)

### RSA

RSA is a public-key cryptosystem that is widely used for secure data transmission.

**Mathematical Representation:**

- **Encryption:** \( C = M^e \mod n \)
- **Decryption:** \( M = C^d \mod n \)

where \( n = p \times q \), and \( e \) and \( d \) are the public and private exponents, respectively.

### Knapsack

The Knapsack problem is a public-key cryptosystem based on the subset sum problem.

**Mathematical Representation:**

- **Encryption:** Sum of selected weights from the public key.
- **Decryption:** Use the private key to solve the subset sum problem.

## Digital Signatures

### RSA Digital Signatures

RSA Digital Signatures use RSA encryption to sign and verify messages.

**Mathematical Representation:**

- **Signing:** \( S = H(M)^d \mod n \)
- **Verification:** \( V = S^e \mod n \)

where \( H(M) \) is the hash of the message.