import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))

while True:
    x = (str(client.recv(1024))).replace("b'", "").replace("'", "")
    print(x.upper())
    if x == 'Current prices and discounts are available here <link>. Other questions you can address our manager by phone: 123 44 55 6666.':
        print('You are welcome!')
        break

    else:
        z = input('Write your answer (or "exit" to quit) here: ')
        if z.lower() != 'exit':
            client.send(bytes(z, encoding='UTF-8'))
        else:
            client.send(bytes(z, encoding='UTF-8'))
            break

client.close()