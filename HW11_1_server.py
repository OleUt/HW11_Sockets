import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5000))
sock.listen(10)
print('server is up now')

while True:
    conn, addr = sock.accept()
    print('client is connected')
    a = conn.recv(1024)
    print('client says:', a)
    conn.send(bytes('Congrats!', encoding='UTF-8'))













