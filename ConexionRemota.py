import paramiko

# Configuración de la conexión
host = '192.168.0.5'
port = 22  # Puerto SSH por defecto
username = 'Julian'
password = 'Hola'

# Crear una instancia del cliente SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conectar al equipo remoto
    client.connect(hostname=host, port=port, username=username, password=password)
    print('Conexión establecida correctamente.')

    # Ejecutar comandos remotos
    stdin, stdout, stderr = client.exec_command('comando_remoto')
    print(stdout.read().decode())

finally:
    # Cerrar la conexión
    client.close()
