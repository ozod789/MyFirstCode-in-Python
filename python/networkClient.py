import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
print(s.recv(1024).decode())
s.send('5'.encode())
print(s.recv(1024).decode())
s.close()