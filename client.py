import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))
s.sendall(bytes('Hello, worlda', encoding="ascii"))
data = s.recv(1024)
print('Am receptionat: ', data)
s.close()