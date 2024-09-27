from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

def get_fernet_key():
    return key
