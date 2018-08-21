import socket
import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8008
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got a connection from ', addr)
    data = c.recv(1024)
    print("button ", data)
    if data == 'Knopf 1':
        keyboard.press("a")  # TODO: in funktion auslagern
    c.send('Thank you for connecting')  # response
    c.close()
