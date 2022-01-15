import socket
from xml.etree.ElementTree import tostring

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
udp_host = socket.gethostname()		
udp_port = 5000	
s.bind((udp_host, udp_port)) 
while True:
    print ("Se asteapta un client...")
    data,addr = s.recvfrom(1024)
    print("Mesaj: ",data," de la ",addr)