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

    # Adjoint matrix: inverse of matrix (over real numbers) * determinant
    matrix_adj = np.round(np.linalg.inv(matrix) * det).astype(int) % mod

    # Final modular inverse matrix
    return (det_inv * matrix_adj) % mod


def preprocess_text(text, block_size=2):
    text = text.upper().replace('J', 'I')  # I/J digabungkan
    text = ''.join(filter(str.isalpha, text))  # hanya ambil huruf
    while len(text) % block_size != 0:
        text += 'X'  # tambahkan X untuk padding
    return text

def text_to_vector(text):
    return [ord(char) - ord('A') for char in text]

def vector_to_text(vector):
    return ''.join(chr(num + ord('A')) for num in vector)

def encrypt(plain_text, key_matrix):
    plain_text = preprocess_text(plain_text)
    key_matrix = np.array(key_matrix)
    cipher_text = ''
    block_size = key_matrix.shape[0]
    for i in range(0, len(plain_text), 2):  # blok 2 huruf
        block = np.array(text_to_vector(plain_text[i:i + 2]))
        cipher_block = np.dot(key_matrix, block) % 26  # kalikan dengan matriks kunci
        cipher_text += vector_to_text(cipher_block)
    return cipher_text

def decrypt(cipher_text, key_matrix):
    cipher_text = preprocess_text(cipher_text)
    key_matrix = np.array(key_matrix)
    cipher_matrix_inv = matrix_inverse(key_matrix)
    plain_text = ''
    for i in range(0, len(cipher_text), 2):
        block = np.array(text_to_vector(cipher_text[i:i + 2]))
        plain_block = np.dot(cipher_matrix_inv, block) % 26
        plain_text += vector_to_text(plain_block)
    return plain_text
