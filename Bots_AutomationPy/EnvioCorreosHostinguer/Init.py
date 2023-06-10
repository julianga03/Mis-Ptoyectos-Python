import os

carpetaPrincipal = "C:/AutomationPy"
carpetaNombreBot = "C:/AutomationPy/TAD-001"
config = "C:/AutomationPy/TAD-001/config"
imput = "C:/AutomationPy/TAD-001/input"
output = "C:/AutomationPy/TAD-001/output"
audit = "C:/AutomationPy/TAD-001/audit"

#Creacion de Carpetas
if not os.path.exists(carpetaPrincipal):
    os.makedirs(carpetaPrincipal)

if not os.path.exists(carpetaNombreBot):
    os.makedirs(carpetaNombreBot)

if not os.path.exists(config):
    os.makedirs(config)

if not os.path.exists(imput):
    os.makedirs(imput)

if not os.path.exists(output):
    os.makedirs(output)

if not os.path.exists(audit):
    os.makedirs(audit)

#_______________________________________

log = "C:/AutomationPy/TAD-001/audit/Envio de correos marketing.txt"
archivo = open(log, "a")