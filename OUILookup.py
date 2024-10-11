#Vicente-Cruces-Collao 21.233.615-7 inf 224
import sys
import getopt
import requests
import time  

def lookup_mac(mac_address):
    
    start_time = time.time()

    
    url = f"https://api.maclookup.app/v2/macs/{mac_address}"
    response = requests.get(url)
    
    
    end_time = time.time()
    response_time = (end_time - start_time) * 1000  

    if response.status_code == 200:
        data = response.json()
        fabricante = data.get('company', 'Fabricante no encontrado')
    else:
        fabricante = "Error al consultar la API."

    return fabricante, response_time  

def main(argv):
    mac_address = ''
    try:
        opts, args = getopt.getopt(argv, "hm:", ["help", "mac="])
    except getopt.GetoptError:
        print('Uso: OUILookup.py --mac <direccion_MAC>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Uso: OUILookup.py --mac <direccion_MAC>')
            sys.exit()
        elif opt in ("-m", "--mac"):
            mac_address = arg
    
    if mac_address:
        fabricante, response_time = lookup_mac(mac_address)
        print(f"MAC address: {mac_address}\nFabricante: {fabricante}\nTiempo de respuesta: {response_time:.2f} ms")
    else:
        print('Uso: OUILookup.py --mac <direccion_MAC>')

if __name__ == "__main__":
    main(sys.argv[1:])
