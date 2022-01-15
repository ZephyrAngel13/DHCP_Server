import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('127.0.0.1', 5000)) 
s.listen(1)
print('Asteapta conexiuni') 
conn, addr = s.accept()
print('S-a conectat clientul', addr, ' la serverul ', conn.getsockname())
while 1:
    data = conn.recv(1024) 
    if not data:
     break
    print('Am receptionat: ', data)
    conn.sendall(bytes('Echo: ' + str(data), encoding="ascii"))
conn.close()