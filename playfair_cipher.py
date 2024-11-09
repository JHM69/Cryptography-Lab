def playfair_encrypt(text, key):
    def generate_key_matrix(key):
        matrix = []
        used = set()
        for char in key.upper():
            if char not in used and char != 'J':
                used.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used:
                used.add(char)
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None

    def process_text(text):
        text = text.upper().replace('J', 'I')
        processed = ""
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                processed += text[i] + 'X'
                i += 1
            elif text[i] == text[i+1]:
                processed += text[i] + 'X'
                i += 1
            else:
                processed += text[i] + text[i+1]
                i += 2
        return processed

    matrix = generate_key_matrix(key)
    text = process_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b] + matrix[row_b][col_a]
    return result

def playfair_decrypt(text, key):
    def generate_key_matrix(key):
        matrix = []
        used = set()
        for char in key.upper():
            if char not in used and char != 'J':
                used.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used:
                used.add(char)
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None

    matrix = generate_key_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            result += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            result += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            result += matrix[row_a][col_b] + matrix[row_b][col_a]
    return result

# Example
text = "JAHANGIR"
key = "JHM69"
encrypted = playfair_encrypt(text, key)
decrypted = playfair_decrypt(encrypted, key)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")