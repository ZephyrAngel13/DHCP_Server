import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host = socket.gethostname()		
udp_port = 5000		
udp_address = (udp_host,udp_port)	        

msg = b"Hello Python!"
print ("UDP target IP:",udp_host)
print ("UDP target Port:",udp_port)

s.sendto(msg,udp_address)