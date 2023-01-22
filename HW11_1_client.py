import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))
client.send(bytes('Hello!', encoding='UTF-8'))
b = client.recv(1024)
print(b)
client.close()
