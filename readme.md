
# Cryptography Algorithms

This project covers various cryptographic algorithms, from classical to modern approaches. Each section includes mathematical foundations, theoretical background, and practical explanations.

## Traditional Ciphers (Monoalphabetic)

### Caesar Cipher

The Caesar Cipher, named after Julius Caesar, is one of the earliest known encryption techniques. It's a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet.

**Mathematical Foundation:**
For a given plaintext letter $P$ and a shift $k$, the ciphertext letter $C$ is:

Encryption: $C \equiv (P + k) \pmod{26}$  
Decryption: $P \equiv (C - k) \pmod{26}$

**Security Analysis:**
- Extremely vulnerable to frequency analysis
- Only 25 possible keys to try (brute force)
- Zero diffusion and confusion properties
- Suitable only for educational purposes

### Multiplicative Cipher

The Multiplicative Cipher extends the Caesar cipher by using multiplication instead of addition. This creates a more complex mapping between plaintext and ciphertext.

**Mathematical Foundation:**
For plaintext $P$ and key $k$:

Encryption: $C \equiv (P \times k) \pmod{26}$  
Decryption: $P \equiv (C \times k^{-1}) \pmod{26}$

Where $k^{-1}$ is the modular multiplicative inverse of $k$.

**Key Selection:**
- $k$ must be coprime with 26 (allowed values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- The existence of $k^{-1}$ is guaranteed when $\gcd(k, 26) = 1$

### Affine Cipher

The Affine Cipher combines both multiplicative and additive (Caesar) components, creating a more complex encryption scheme.

**Mathematical Foundation:**
For plaintext $P$ and keys $a, b$:

Encryption: $C \equiv (a \times P + b) \pmod{26}$  
Decryption: $P \equiv a^{-1}(C - b) \pmod{26}$

**Security Considerations:**
- Still vulnerable to frequency analysis
- Total key space is $\varphi(26) \times 26 = 12 \times 26 = 312$ possible keys
- Provides slightly better security than Caesar but still not secure for modern use

## Polyalphabetic Ciphers

### Autokey Cipher

The Autokey Cipher improves upon simple substitution by using a keyword and the plaintext itself to generate the keystream.

**Mathematical Foundation:**
For plaintext $P[i]$ and keystream $K[i]$:

Encryption: $C[i] \equiv (P[i] + K[i]) \pmod{26}$  
Decryption: $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**Key Generation:**
1. Start with the keyword
2. Append the plaintext (except last character)
3. Use this combined string as the keystream

### Vigenère Cipher

The Vigenère Cipher was considered "le chiffre indéchiffrable" (the unbreakable cipher) for centuries.

**Mathematical Foundation:**
For plaintext $P[i]$ and key $K[i]$:

Encryption: $C[i] \equiv (P[i] + K[i]) \pmod{26}$  
Decryption: $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**Security Features:**
- Resistant to simple frequency analysis
- Key length determines security strength
- Vulnerable to Kasiski examination and index of coincidence analysis

### Hill Cipher

The Hill Cipher introduces the concept of matrix operations in cryptography, encrypting blocks of text using linear algebra.

**Mathematical Foundation:**
For $n \times n$ key matrix $K$:

Encryption: $C = K \times P \pmod{26}$  
Decryption: $P = K^{-1} \times C \pmod{26}$

**Requirements:**
- Key matrix must be invertible modulo 26
- Determinant must be coprime with 26
- Increased complexity with larger matrices

### One-Time Pad

The One-Time Pad is the only theoretically unbreakable cipher when used correctly.

**Mathematical Foundation:**
For each character position $i$:

Encryption: $C[i] \equiv (P[i] + K[i]) \pmod{26}$  
Decryption: $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**Security Requirements:**
1. Key must be truly random
2. Key must be at least as long as the message
3. Key must never be reused
4. Key must be kept completely secret

## Modern Block Ciphers

### AES (Advanced Encryption Standard)

AES is the current standard for symmetric encryption, operating on 128-bit blocks.

**Core Operations:**
1. **SubBytes**: Non-linear substitution
2. **ShiftRows**: Permutation step
3. **MixColumns**: Linear mixing
4. **AddRoundKey**: Key incorporation

**Mathematical Foundation:**
- Operations in Galois Field $GF(2^8)$
- MixColumns multiplication matrix:

$$
\begin{pmatrix}
2 & 3 & 1 & 1 \\
1 & 2 & 3 & 1 \\
1 & 1 & 2 & 3 \\
3 & 1 & 1 & 2 \\
\end{pmatrix}
$$

### RSA

RSA security is based on the difficulty of factoring large numbers.

**Mathematical Foundation:**
1. Choose primes $p, q$
2. $n = p \times q$
3. $\phi(n) = (p - 1)(q - 1)$
4. Choose $e$ where $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$
5. Calculate $d$ where $d \times e \equiv 1 \pmod{\phi(n)}$

**Operations:**
- Encryption: $C \equiv M^e \pmod{n}$
- Decryption: $M \equiv C^d \pmod{n}$

**Security Considerations:**
- Key size typically 2048 or 4096 bits
- Vulnerable to quantum computers (Shor's algorithm)
- Relies on proper padding (PKCS#1 v2.1)

### ElGamal

ElGamal is based on the Diffie-Hellman key exchange and the discrete logarithm problem.

**Mathematical Foundation:**
Setup:
1. Choose prime $p$ and generator $g$
2. Select private key $x$
3. Calculate public key $y = g^x \pmod{p}$

**Operations:**
Encryption (with random $k$):
- $C_1 = g^k \pmod{p}$
- $C_2 = M \times y^k \pmod{p}$

Decryption:
- $M = C_2 \times (C_1^x)^{-1} \pmod{p}$

## Digital Signatures

### RSA Digital Signatures

RSA signatures provide authentication and non-repudiation.

**Mathematical Foundation:**
- Signing: $S \equiv H(M)^d \pmod{n}$
- Verification: $H(M) \equiv S^e \pmod{n}$

Where $H(M)$ is a cryptographic hash function.

**Security Properties:**
1. **Authentication**: Verifies the signer's identity
2. **Non-repudiation**: Signer cannot deny signing
3. **Integrity**: Message cannot be modified
4. Uses same key pairs as RSA encryption

