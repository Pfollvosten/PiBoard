import threading
import socket
import time
from threading import Thread

class Server:
    thread = Thread()

    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object
        host = "192.168.178.22"                                 # Get local machine name
        port = 8765                                             # Reserve a port for your service.
        s.bind((host, port))                                    # Bind to the port
        s.listen(1)                                             # Now wait for client connection.
        run_forever(self)

    #SERVER
    """keep the server up"""
    def run_forever(self):
        # runnning forever
        while True:
            c, addr = self.s.accept()                                # Establish connection with client.
            print ('Got connection from', addr)                 # show the client connection
            data = c.recv(1024)                                 # get data sent from client
            print(data)
            c.send('Thank you for connecting'.encode())         # message the client
            c.close()                                           # Close the connection