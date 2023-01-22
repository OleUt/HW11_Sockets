import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))

phrase = input('Type your text: ')
client.send(bytes(phrase, encoding='UTF-8'))
words = client.recv(1024)
print(words)

client.close()
