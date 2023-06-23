from scapy.all import ARP, Ether, srp
import socket
import requests

def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    return "Desconocido"

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Desconocido"

def scan_devices(ip_range):
    # Crea una solicitud ARP para escanear la red
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Envía y recibe paquetes ARP utilizando srp() de Scapy
    result = srp(packet, timeout=3, verbose=0)[0]

    # Recorre los resultados y muestra la información de los dispositivos
    devices = []
    for sent, received in result:
        vendor = get_vendor(received.hwsrc)
        hostname = get_hostname(received.psrc)
        devices.append({'IP': received.psrc, 'MAC': received.hwsrc, 'Vendor': vendor, 'Hostname': hostname})

    # Retorna la lista de dispositivos encontrados
    return devices

# Llama a la función para escanear los dispositivos conectados por cable
wired_devices = scan_devices("192.168.1.1/24")

# Llama a la función para escanear los dispositivos conectados por WiFi
wifi_devices = scan_devices("192.168.0.1/24")

# Combina las listas de dispositivos encontrados
devices = wired_devices + wifi_devices

# Imprime la información de los dispositivos encontrados
for device in devices:
    print("IP:", device['IP'], "MAC:", device['MAC'], "Vendor:", device['Vendor'], "Hostname:", device['Hostname'])


#instalar https://npcap.org/ para que funcione