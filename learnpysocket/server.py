# Echo server program
import socket
import sys

HOST = '2400:dd01:1020:70:31e3:35b:ab69:aee4'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
    data,ip=s.recvfrom(1024)
    print data,ip,'-----------'
s.close()
