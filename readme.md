# Cryptography Algorithms

This project covers various cryptographic algorithms, from classical to modern approaches. Each section includes mathematical foundations, theoretical background, and practical explanations.

## Table of Contents

- [Traditional Ciphers (Monoalphabetic)](#traditional-ciphers-monoalphabetic)
  - [Caesar Cipher](#caesar-cipher)
  - [Multiplicative Cipher](#multiplicative-cipher)
  - [Affine Cipher](#affine-cipher)
- [Polyalphabetic Ciphers](#polyalphabetic-ciphers)
  - [Autokey Cipher](#autokey-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
  - [Hill Cipher](#hill-cipher)
  - [One-Time Pad](#one-time-pad)
- [Modern Block Ciphers](#modern-block-ciphers)
  - [DES (Data Encryption Standard)](#des-data-encryption-standard)
  - [AES (Advanced Encryption Standard)](#aes-advanced-encryption-standard)
- [Asymmetric Encryption Algorithms](#asymmetric-encryption-algorithms)
  - [RSA](#rsa)
  - [ElGamal](#elgamal)
- [Digital Signatures](#digital-signatures)
  - [RSA Digital Signatures](#rsa-digital-signatures)

## Traditional Ciphers (Monoalphabetic)

### Caesar Cipher

The **Caesar Cipher**, named after Julius Caesar, is one of the earliest known encryption techniques. It's a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet.

**Mathematical Foundation:**

For a given plaintext letter $P$ and a shift $k$, the ciphertext letter $C$ is calculated as:

- **Encryption:** $C \equiv (P + k) \pmod{26}$
- **Decryption:** $P \equiv (C - k) \pmod{26}$

**How It Works:**

1. **Choose a Shift Key ($k$):** This is a number between 1 and 25.
2. **Encrypt the Message:**
   - Replace each letter in the plaintext with the letter $k$ positions down the alphabet.
   - Wrap around to the beginning if necessary.
3. **Decrypt the Message:**
   - Shift each letter in the ciphertext $k$ positions up the alphabet.

**Security Analysis:**

- **Vulnerabilities:**
  - Extremely susceptible to frequency analysis.
  - Only 25 possible keys make it easy to brute-force.
- **Use Cases:**
  - Educational purposes.
  - Not suitable for serious communication.

### Multiplicative Cipher

The **Multiplicative Cipher** extends the Caesar cipher by using multiplication instead of addition, creating a more complex mapping between plaintext and ciphertext.

**Mathematical Foundation:**

For plaintext $P$ and key $k$:

- **Encryption:** $C \equiv (P \times k) \pmod{26}$
- **Decryption:** $P \equiv (C \times k^{-1}) \pmod{26}$

Where $k^{-1}$ is the modular multiplicative inverse of $k$ modulo 26.

**How It Works:**

1. **Choose a Key ($k$):** Must be an integer coprime with 26.
2. **Calculate Modular Inverse ($k^{-1}$):**
   - Ensures decryption is possible.
3. **Encrypt the Message:**
   - Multiply each plaintext letter's numerical equivalent by $k$ modulo 26.
4. **Decrypt the Message:**
   - Multiply each ciphertext letter by $k^{-1}$ modulo 26.

**Key Selection:**

- Valid keys are integers where $\gcd(k, 26) = 1$.
- Allowed values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

**Security Considerations:**

- Slightly more secure than the Caesar Cipher.
- Still vulnerable to frequency analysis.

### Affine Cipher

The **Affine Cipher** combines both multiplicative and additive components, offering a more complex encryption scheme.

**Mathematical Foundation:**

For plaintext $P$ and keys $a$, $b$:

- **Encryption:** $C \equiv (a \times P + b) \pmod{26}$
- **Decryption:** $P \equiv a^{-1}(C - b) \pmod{26}$

Where $a^{-1}$ is the modular inverse of $a$ modulo 26.

**How It Works:**

1. **Choose Keys ($a$, $b$):**
   - $a$ must be coprime with 26.
   - $b$ can be any integer between 0 and 25.
2. **Encrypt the Message:**
   - Apply the affine transformation to each letter.
3. **Decrypt the Message:**
   - Use the modular inverse $a^{-1}$ to reverse the transformation.

**Security Considerations:**

- Total key space of 312 possible keys.
- More secure than Caesar and Multiplicative ciphers but still inadequate for modern use.

## Polyalphabetic Ciphers

### Autokey Cipher

The **Autokey Cipher** enhances simple substitution by incorporating the plaintext into the key, generating a more dynamic keystream.

**Mathematical Foundation:**

For plaintext $P[i]$ and keystream $K[i]$:

- **Encryption:** $C[i] \equiv (P[i] + K[i]) \pmod{26}$
- **Decryption:** $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**How It Works:**

1. **Key Generation:**
   - Start with a keyword.
   - Append plaintext letters to the keyword to create the keystream.
2. **Encrypt the Message:**
   - Add each plaintext letter to the corresponding keystream letter modulo 26.
3. **Decrypt the Message:**
   - Subtract the keystream letter from each ciphertext letter modulo 26.

**Security Features:**

- Reduces patterns that can be exploited by frequency analysis.
- Key is as long as the message, improving security.

### Vigenère Cipher

The **Vigenère Cipher** uses a repeating keyword to shift letters, providing resistance against frequency analysis.

**Mathematical Foundation:**

For plaintext $P[i]$ and key $K[i]$:

- **Encryption:** $C[i] \equiv (P[i] + K[i]) \pmod{26}$
- **Decryption:** $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**How It Works:**

1. **Choose a Keyword:**
   - Determines the sequence of shifts.
2. **Extend the Keyword:**
   - Repeat the keyword to match the length of the plaintext.
3. **Encrypt the Message:**
   - Shift each plaintext letter by the numerical equivalent of the corresponding keyword letter.
4. **Decrypt the Message:**
   - Reverse the shift using the keyword.

**Security Features:**

- Hides letter frequencies better than monoalphabetic ciphers.
- Vulnerable to advanced methods like Kasiski examination.

### Hill Cipher

The **Hill Cipher** introduces linear algebra into cryptography, encrypting blocks of text using matrix multiplication.

**Mathematical Foundation:**

For $n \times n$ key matrix $K$ and plaintext vector $P$:

- **Encryption:** $C = K \times P \pmod{26}$
- **Decryption:** $P = K^{-1} \times C \pmod{26}$

**How It Works:**

1. **Key Matrix Selection:**
   - Choose an invertible matrix $K$ modulo 26.
2. **Encrypt the Message:**
   - Divide plaintext into vectors of size $n$.
   - Multiply each vector by $K$ modulo 26.
3. **Decrypt the Message:**
   - Compute the inverse matrix $K^{-1}$ modulo 26.
   - Multiply ciphertext vectors by $K^{-1}$ modulo 26.

**Requirements:**

- Determinant of $K$ must be coprime with 26.
- Larger matrix sizes increase security but complicate computation.

**Security Considerations:**

- More secure than earlier ciphers due to block encryption.
- Vulnerable if attackers have enough plaintext-ciphertext pairs.

### One-Time Pad

The **One-Time Pad** is theoretically unbreakable when used correctly, employing a random key that is as long as the message.

**Mathematical Foundation:**

For each character position $i$:

- **Encryption:** $C[i] \equiv (P[i] + K[i]) \pmod{26}$
- **Decryption:** $P[i] \equiv (C[i] - K[i]) \pmod{26}$

**How It Works:**

1. **Key Generation:**
   - Generate a truly random key of the same length as the message.
2. **Encrypt the Message:**
   - Add each plaintext letter to the corresponding key letter modulo 26.
3. **Decrypt the Message:**
   - Subtract the key letter from each ciphertext letter modulo 26.

**Security Requirements:**

- Key must be used only once.
- Key must remain completely secret.
- Key must be truly random, not generated by a pseudorandom algorithm.

**Security Features:**

- Offers perfect secrecy.
- Impractical for most uses due to key management challenges.

## Modern Block Ciphers

### DES (Data Encryption Standard)

**DES** was a widely used symmetric-key algorithm for encrypting electronic data, now considered insecure due to its small key size.

**Mathematical Foundation:**

- Operates on 64-bit blocks.
- Uses a 56-bit key (originally a 64-bit key with 8 parity bits).

**How It Works:**

1. **Initial Permutation (IP):**
   - Rearranges the bits in the plaintext.
2. **16 Rounds of Feistel Function:**
   - Splits data into Left ($L$) and Right ($R$) halves.
   - Each round applies a round key to $R$ and combines it with $L$.
   - Uses substitution and permutation (S-boxes and P-boxes).
3. **Final Permutation (FP):**
   - Inverse of the initial permutation.

**Security Considerations:**

- Vulnerable to brute-force attacks due to the small key size.
- Superseded by Triple DES and AES.

### AES (Advanced Encryption Standard)

**AES** is the current standard for symmetric encryption, designed to be secure and efficient.

**Mathematical Foundation:**

- Operates on 128-bit blocks.
- Key sizes: 128, 192, or 256 bits.
- Uses operations in the Galois Field $GF(2^8)$.

**How It Works:**

1. **Initial Round:**
   - **AddRoundKey:** Combines the plaintext with the initial key.
2. **Main Rounds (Nr = 10, 12, or 14):**
   - **SubBytes:** Applies a non-linear substitution using an S-box.
   - **ShiftRows:** Cyclically shifts rows of the state array.
   - **MixColumns:** Combines bytes within each column using linear transformation.
   - **AddRoundKey:** Integrates round key with the state.
3. **Final Round:**
   - Omits the **MixColumns** step.

**Core Operations:**

- **SubBytes:** Uses an S-box based on multiplicative inverses in $GF(2^8)$.
- **ShiftRows:** Provides diffusion by shifting bytes in each row.
- **MixColumns:** Uses a fixed matrix multiplication over $GF(2^8)$:

  $$
  \begin{pmatrix}
  2 & 3 & 1 & 1 \\
  1 & 2 & 3 & 1 \\
  1 & 1 & 2 & 3 \\
  3 & 1 & 1 & 2 \\
  \end{pmatrix}
  $$

- **AddRoundKey:** Combines the state with the round key using bitwise XOR.

**Security Features:**

- Resistant to known attacks.
- Efficient in both hardware and software implementations.
- Key-dependent transformations enhance security.

## Asymmetric Encryption Algorithms

### RSA

**RSA** is one of the first public-key cryptosystems and is widely used for secure data transmission.

**Mathematical Foundation:**

1. **Key Generation:**
   - Choose two large prime numbers $p$ and $q$.
   - Compute $n = p \times q$.
   - Calculate the totient $\phi(n) = (p - 1)(q - 1)$.
   - Choose an integer $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
   - Determine $d$ as the modular inverse of $e$ modulo $\phi(n)$: $d \times e \equiv 1 \pmod{\phi(n)}$.
2. **Public Key:** $(e, n)$
3. **Private Key:** $(d, n)$

**How It Works:**

- **Encryption:**
  - Ciphertext: $C \equiv M^e \pmod{n}$
- **Decryption:**
  - Plaintext: $M \equiv C^d \pmod{n}$

**Security Considerations:**

- Security relies on the difficulty of factoring large integers.
- Key sizes of at least 2048 bits are recommended.
- Vulnerable to quantum attacks (Shor's algorithm).

### ElGamal

**ElGamal** is an asymmetric key encryption algorithm based on the Diffie-Hellman key exchange.

**Mathematical Foundation:**

1. **Key Generation:**
   - Choose a large prime $p$ and a generator $g$ of the multiplicative group of integers modulo $p$.
   - Select a private key $x$ randomly from $\{1, 2, ..., p-2\}$.
   - Compute the public key $y = g^x \pmod{p}$.
2. **Public Key:** $(p, g, y)$
3. **Private Key:** $x$

**How It Works:**

- **Encryption:**
  - Choose a random integer $k$ from $\{1, 2, ..., p-2\}$.
  - Compute $C_1 = g^k \pmod{p}$.
  - Compute $C_2 = M \times y^k \pmod{p}$.
  - Ciphertext: $(C_1, C_2)$
- **Decryption:**
  - Compute $s = C_1^x \pmod{p}$.
  - Compute $s^{-1}$, the modular inverse of $s$.
  - Recover plaintext: $M = C_2 \times s^{-1} \pmod{p}$.

**Security Considerations:**

- Security is based on the difficulty of solving the discrete logarithm problem.
- Requires randomness in encryption, enhancing security.

## Digital Signatures

### RSA Digital Signatures

**RSA signatures** provide a method for verifying the authenticity and integrity of a message.

**Mathematical Foundation:**

- **Signing:**
  - Compute the hash $H(M)$ of the message $M$.
  - Signature: $S \equiv H(M)^d \pmod{n}$
- **Verification:**
  - Compute $H(M)$.
  - Verify: $H(M) \equiv S^e \pmod{n}$

**How It Works:**

1. **Sender Generates Signature:**
   - Hashes the message to create a message digest.
   - Encrypts the digest with their private key.
2. **Receiver Verifies Signature:**
   - Decrypts the signature using the sender's public key.
   - Compares the decrypted hash with their own hash of the message.

**Security Properties:**

1. **Authentication:** Confirms the identity of the sender.
2. **Non-repudiation:** Sender cannot deny the authenticity of the message.
3. **Integrity:** Ensures the message has not been altered.

**Considerations:**

- Uses the same mathematical principles as RSA encryption.
- Relies on secure hash functions like SHA-256.

---
