def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J digabung
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # hapus duplikat dan urutkan
    matrix = "".join(sorted(set(key + alphabet), key=lambda x: (key + alphabet).index(x)))
    matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
    return matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j
    return None, None

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text.append(text[i] + 'X')  # jika ada huruf yang sama, tambahkan X
            i += 1
        else:
            processed_text.append(text[i:i + 2])  # pasangan huruf
            i += 2
    if len(processed_text[-1]) == 1:  # kalau teks terakhir hanya satu huruf, tambahkan X
        processed_text[-1] += 'X'
    return processed_text

def encrypt(plain_text, key):
    matrix = create_matrix(key)
    text_pairs = preprocess_text(plain_text)
    cipher_text = ""
    for pair in text_pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:  # same row, shift columns
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # same column, shift rows
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:  # rectangle, swap corners
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]
    
    return cipher_text

def decrypt(cipher_text, key):
    matrix = create_matrix(key)
    text_pairs = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]
    plain_text = ""
    for pair in text_pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:  # same row, shift columns
            plain_text += matrix[row1][(col1 - 1) % 5]
            plain_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # same column, shift rows
            plain_text += matrix[(row1 - 1) % 5][col1]
            plain_text += matrix[(row2 - 1) % 5][col2]
        else:  # rectangle, swap corners
            plain_text += matrix[row1][col2]
            plain_text += matrix[row2][col1]
    
    return plain_text
