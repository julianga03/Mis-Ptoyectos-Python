import win32cred

# Definir el nombre del objetivo (target_name)
target_name = "Prueba"  # Reemplaza con el nombre correcto

try:
    # Obtener credenciales guardadas
    credential = win32cred.CredRead(target_name, win32cred.CRED_TYPE_GENERIC, 0)
except Exception as e:
    print(f"No se pudieron leer las credenciales: {e}")
    # Puedes manejar la excepción de acuerdo a tus necesidades
    # Por ejemplo, puedes pedir al usuario que ingrese manualmente las credenciales

# Decodificar la cadena de bytes a una cadena de caracteres unicode

password_unicode = credential['CredentialBlob']
print(password_unicode)
password_unicode = credential['CredentialBlob'].decode('utf-16')

# Iniciar sesión en la aplicación utilizando las credenciales recuperadas
# Aquí deberías tener el código real para la función 'login' antes de esta línea
# En este ejemplo, simplemente imprimimos los datos de inicio de sesión
print(f"Intento de inicio de sesión con usuario: {credential['UserName']}, contraseña: {password_unicode}")
