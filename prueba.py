import imaplib
import email
from email.header import decode_header
from unidecode import unidecode

RUTA_LOG = r"C:\ProgramData\MyBots\004 - Datacredito\Temp\Informacion XML.txt"

# Configurar Credenciales
email_address = 'juliangalindo3214@gmail.com'
password = 'nckqmrxgrcyxfjml'

# Conéctar al servidor IMAP de Gmail
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_address, password)

# Seleccionar la carpeta "Recibidos" (Inbox)
mail.select('Inbox')

# Realizar una búsqueda utilizando el filtro X-GM-RAW para excluir etiquetas específicas
status, message_numbers = mail.search(None, 'X-GM-RAW "category:primary is:unread -label:social -label:promotions"')

if status == 'OK':
    message_numbers = message_numbers[0].split()
    for num in message_numbers:
        status, message_data = mail.fetch(num, '(RFC822)')
        if status == 'OK':
            raw_email = message_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Decodifica el asunto (puede contener caracteres especiales)
            subject, encoding = decode_header(msg['Subject'])[0]
            if encoding:
                subject = subject.decode(encoding)
                subject = unidecode(subject)
            print(subject)
            mail.store(num, '-FLAGS', '(\Seen)') # Esto marca el correo como no leído

            if subject.lower() == "codigo":
                #mail.store(num, '-FLAGS', '(\Seen)') # Esto marca el correo como no leído
                mail.store(num, '+FLAGS', '(\Seen)') # Esto marca el correo como leído
                #mail.store(num, '+FLAGS', '(\Deleted)') # Esto Borra el correo

                #Extraer el cuerpo del correo
                if msg.is_multipart():
                    body=''
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if "attachment" not in content_disposition:
                            body += part.get_payload(decode=True).decode('utf-8', 'ignore')

                else:
                    body = msg.get_payload(decode=True).decode('utf-8', 'ignore')

                # Almacenar el cuerpo en una variable
                codigo_body = body
                #print(codigo_body)

                with open(RUTA_LOG, "w") as archivo:
                    archivo.write(codigo_body)

# Cierra la conexión
mail.logout()
print("saliocorreo")