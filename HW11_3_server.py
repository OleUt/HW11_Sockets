import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5000))
sock.listen(5)
print('server is up now')

def word_counter(text):
    words = len(text.split(' '))
    return words

while True:
    conn, addr = sock.accept()
    print('client is connected')
    text = str(conn.recv(1024))
    words = 'There are ' + str(word_counter(text)) + ' words in the text.'
    conn.send(bytes(words, encoding='UTF-8'))
