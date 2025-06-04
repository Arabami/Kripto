import numpy as np

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_inverse(matrix, mod=26):
    det = int(round(np.linalg.det(matrix))) % mod
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise Exception("Matrix is not invertible")
    matrix_adj = np.round(np.linalg.inv(matrix) * det).astype(int) % mod
    return (det_inv * matrix_adj) % mod

def preprocess_text(text, block_size):
    text = text.upper().replace('J', 'I')  # Replace J with I
    text = ''.join(filter(str.isalpha, text))  # Keep only letters
    while len(text) % block_size != 0:
        text += 'X'  # Padding
    return text

def text_to_vector(text):
    return [ord(char) - ord('A') for char in text]

def vector_to_text(vector):
    return ''.join(chr(int(num) + ord('A')) for num in vector)

def encrypt(plain_text, key_matrix):
    key_matrix = np.array(key_matrix)
    block_size = key_matrix.shape[0]
    plain_text = preprocess_text(plain_text, block_size)
    cipher_text = ''
    for i in range(0, len(plain_text), block_size):
        block = np.array(text_to_vector(plain_text[i:i + block_size]))
        block = block.reshape(-1, 1)
        cipher_block = np.dot(key_matrix, block) % 26
        cipher_text += vector_to_text(cipher_block.flatten())
    return cipher_text

def decrypt(cipher_text, key_matrix):
    key_matrix = np.array(key_matrix)
    block_size = key_matrix.shape[0]
    cipher_text = preprocess_text(cipher_text, block_size)
    cipher_matrix_inv = matrix_inverse(key_matrix)
    plain_text = ''
    for i in range(0, len(cipher_text), block_size):
        block = np.array(text_to_vector(cipher_text[i:i + block_size]))
        block = block.reshape(-1, 1)
        plain_block = np.dot(cipher_matrix_inv, block) % 26
        plain_text += vector_to_text(plain_block.flatten())
    return plain_text
