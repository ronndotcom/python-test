#! /usr/bin/env python
import socket
import sys
 
HOST = 'localhost'
GET = 'faulty'
PORT = int(sys.argv[1])
 
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)
 
try:
  sock.connect((HOST, PORT))
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)
 
sock.send("GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (GET, HOST))
 
data = sock.recv(1024)
string = ""
while len(data):
  string = string + data
  data = sock.recv(1024)
sock.close()
 
print string
 
sys.exit(0)