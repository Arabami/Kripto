import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'cipher_algorithms')))

from vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
from vigenere_auto import encrypt as vigenere_auto_encrypt, decrypt as vigenere_auto_decrypt
from vigenere_extended import encrypt as vigenere_extended_encrypt, decrypt as vigenere_extended_decrypt
from affine import encrypt as affine_encrypt, decrypt as affine_decrypt
from playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt
from hill import encrypt as hill_encrypt, decrypt as hill_decrypt
import numpy as np

def test_vigenere():
    text = "HELLO"
    key = "KEY"
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Vigenere Encrypt: {encrypted}")
    print(f"Vigenere Decrypt: {decrypted}")

def test_vigenere_auto():
    text = "HELLO"
    key = "KEY"
    encrypted = vigenere_auto_encrypt(text, key)
    decrypted = vigenere_auto_decrypt(encrypted, key)
    print(f"Auto-key Vigenere Encrypt: {encrypted}")
    print(f"Auto-key Vigenere Decrypt: {decrypted}")

def test_vigenere_extended():
    text = "HELLO"
    key = "KEY"
    encrypted = vigenere_extended_encrypt(text.encode('latin1'), key)
    decrypted = vigenere_extended_decrypt(encrypted, key).decode('latin1')
    print(f"Extended Vigenere Encrypt: {encrypted}")
    print(f"Extended Vigenere Decrypt: {decrypted}")

def test_affine():
    text = "HELLO"
    a, b = 5, 8
    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)
    print(f"Affine Encrypt: {encrypted}")
    print(f"Affine Decrypt: {decrypted}")

def test_playfair():
    text = "HELLO"
    key = "KEYWORD"
    encrypted = playfair_encrypt(text, key)
    decrypted = playfair_decrypt(encrypted, key)
    print(f"Playfair Encrypt: {encrypted}")
    print(f"Playfair Decrypt: {decrypted}")

def test_hill():
    text = "HELLO"
    key_matrix = np.array([[6, 24], [1, 16]])  # 2x2 matrix
    encrypted = hill_encrypt(text, key_matrix)
    decrypted = hill_decrypt(encrypted, key_matrix)
    print(f"Hill Encrypt: {encrypted}")
    print(f"Hill Decrypt: {decrypted}")

if __name__ == "__main__":
    print("Testing Vigenere Cipher:")
    test_vigenere()
    print("\nTesting Auto-key Vigenere Cipher:")
    test_vigenere_auto()
    print("\nTesting Extended Vigenere Cipher:")
    test_vigenere_extended()
    print("\nTesting Affine Cipher:")
    test_affine()
    print("\nTesting Playfair Cipher:")
    test_playfair()
    print("\nTesting Hill Cipher:")
    test_hill()
