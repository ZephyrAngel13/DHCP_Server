import socket
import time

#Constante DHCP
DHCP_DISCOVER = 1
DHCP_OFFER = 2
DHCP_REQUEST = 3
DHCP_DECLINE = 4
DHCP_ACK = 5
DHCP_NAK = 6
#Mesajele transmise de un client DHCP sunt de DISCOVER, REQUEST sau DECLINE
#Mesajele transmise de un server DHCP sunt de OFFER sau de ACK/NACK

#Tipuri de variabile
INT = '_int'  #integer
HEX = '_hex'  #hexadecimal
IP = '_ip'    #tip IP / identificator unic al unui nod dintr-o retea de calculatoare locala(10.0.0.96/192.168.0.3/127.0.0.100) sau publice (142.251.39.78-google.com)
MAC = '_mac'  #tip MAC / identificator unic al unui device dat de producator(AF-68-65-38-88-1A)
STR = '_str'  #string(sir de caractere)

IP="127.0.0.0"

#Format mesaj DHCP
DHCP_FIELDS = [
    {'id': 'op', 'name': 'message_type', 'length': 1, 'type': INT},
    {'id': 'htype', 'name': 'hardware_type', 'length': 1, 'type': INT},
    {'id': 'hlen', 'name': 'hardware_address_length', 'length': 1, 'type': INT},
    {'id': 'hops', 'name': 'hops', 'length': 1, 'type': INT},
    {'id': 'xid', 'name': 'transaction_id', 'length': 4, 'type': HEX},
    {'id': 'secs', 'name': 'seconds_elapsed', 'length': 2, 'type': INT},
    {'id': 'flags', 'name': 'boot_flags', 'length': 2, 'type': HEX},
    {'id': 'ciaddr', 'name': 'client_ip', 'length': 4, 'type': IP},
    {'id': 'yiaddr', 'name': 'your_ip', 'length': 4, 'type': IP},
    {'id': 'siaddr', 'name': 'next_server_ip', 'length': 4, 'type': IP},
    {'id': 'giaddr', 'name': 'relay_agent_ip', 'length': 4, 'type': IP},
    {'id': 'chaddr', 'name': 'client_mac', 'length': 16, 'type': MAC},
    {'id': 'sname', 'name': 'server_hostname', 'length': 64, 'type': STR},
    {'id': 'filename', 'name': 'boot_filename', 'length': 128, 'type': STR},
    {'id': 'magic', 'name': 'magic_cookie', 'length': 4, 'type': HEX},
]


class DHCP_Packet(object):
    def __init__(self):
        self.msg_type=None
    
class Lease(object):
    def __init__(self,ip=None, mac=None):
        self.ip = ip
        self.mac = mac
        self.lease_time = time.time()
        
class Leases(object):
    def __init__(self):
        self.leases= []
        

class Server(object):
    def __init__(self):
        self.port = 67
        self.ip=IP
        self.sock=None

        self.create_lease_db()
        self.bind()

    def bind(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#socket-ul va transmite date in regim UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#socket-ul va reutiliza adresa asignata atunci cand va fi utilizata functia bind() a doua oara, altfel fara aceasta optiune, adresa asignata va ramane blocata
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)#socket-ul va face broadcast pe adresa de broadcast 255.255.255.255
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, self.interface)#socket-ul va fi asignat device-ului care a lansat in executie programul
        self.sock.bind((self.ip, self.port))#socket-ului i-se asigneaza adresa IP selectata la inceputul programului static si portul asignat in initializare(67- port specific pentru serverele DHCP)

    def create_lease_db(self):
        self.subnet=self.ip



if __name__ == "__main__":
    d=Server()
    d.start_server()