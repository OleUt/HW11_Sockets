import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5000))
sock.listen(10)
print('server is up now')


def gym_chat_bot():

    try:
        conn.send(bytes('Hello! What do you prefer - gym or group workouts?', encoding='UTF-8'))
        a = str(conn.recv(1024)).replace("b'", "").replace("'", "").lower()
        if a == 'exit':
             raise Exception

        aaa = 'other'
        for aa in a.split():
            if aa == 'gym':
                aaa = 'gym'

        if aaa == 'gym':
            conn.send(bytes('Great! Do you need a personal trainer?', encoding='UTF-8'))
            b = str(conn.recv(1024)).replace("b'", "").replace("'", "").lower()
            if b == 'exit':
                raise Exception
            if b == 'not' or b == 'no' or b == 'n':
                conn.send(bytes('You can choose time for visiting here <link>. Do you have some other questions?', encoding='UTF-8'))
                a = str(conn.recv(1024)).replace("b'", "").replace("'", "").lower()
                if a == 'exit':
                    raise Exception
            else:
                conn.send(bytes('You can choose your trainer here <link>. Do you have some other questions?', encoding='UTF-8'))
                a = str(conn.recv(1024)).replace("b'", "").replace("'", "").lower()
                if a == 'exit':
                    raise Exception
        else:
            conn.send(bytes('Great! You can find our workout schedule here <link>. Do you have some other questions?', encoding='UTF-8'))
            a = str(conn.recv(1024)).replace("b'", "").replace("'", "").lower()
            if a == 'exit':
                raise Exception

        conn.send(bytes('Current prices and discounts are available here <link>. Other questions you can address our manager by phone: 123 44 55 6666.', encoding='UTF-8'))

    except Exception: 'exit'


while True:
    conn, addr = sock.accept()
    print('client is connected')
    gym_chat_bot()
    print('client has left the chat')
    #break

