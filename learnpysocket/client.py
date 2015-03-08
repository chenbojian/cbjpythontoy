# Echo server program
import socket
import sys

HOST = '2400:dd01:1020:70:31e3:35b:ab69:aee4'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
#s.connect((HOST,PORT))
while True:
    data=raw_input()
    s.sendto(data,(HOST,PORT))
s.close()
