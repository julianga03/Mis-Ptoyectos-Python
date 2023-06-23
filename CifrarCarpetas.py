import pyAesCrypt
import os

def encrypt_folder(folder_path, password):
    # Nombre del archivo encriptado
    encrypted_file = folder_path + ".aes"

    # Comprimir y encriptar la carpeta
    pyAesCrypt.encryptFile(folder_path, encrypted_file, password)

    # Eliminar la carpeta original
    os.remove(folder_path)
    
def decrypt_folder(encrypted_file, password):
    # Nombre de la carpeta desencriptada
    decrypted_folder = encrypted_file[:-4]

    # Desencriptar y descomprimir la carpeta
    pyAesCrypt.decryptFile(encrypted_file, decrypted_folder, password)

    # Eliminar el archivo encriptado
    os.remove(encrypted_file)

# Ruta de la carpeta a encriptar
folder_path = r"C:\Users\julia\OneDrive\Desktop\Julian"

# Contraseña para encriptar y desencriptar
password = "Prueba"

# Encriptar la carpeta
encrypt_folder(folder_path, password)

# Desencriptar la carpeta
decrypt_folder(folder_path + ".aes", password)
