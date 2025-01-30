import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("encryption_key.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python encryptor.py <encrypt/decrypt> <arquivo>")
        sys.exit(1)
    
    action = sys.argv[1]
    target_file = sys.argv[2]
    
    if action == "encrypt":
        key = generate_key()
        encrypt_file(target_file, key)
        print("Arquivo criptografado com sucesso!")
    elif action == "decrypt":
        key = load_key()
        decrypt_file(target_file, key)
        print("Arquivo descriptografado com sucesso!")
    else:
        print("Ação inválida! Use 'encrypt' ou 'decrypt'")
        sys.exit(1)
