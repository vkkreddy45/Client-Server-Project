
# Import socket module
import socket            

#Import sys module
import sys

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 8787               
 
# connect to the server on local computer
# sys.argv[1] - contains the server ip address
print("Connecting to server")
s.connect((sys.argv[1], port))
 
# receive acknowledgement from the server and decoding to get the string.
print(s.recv(1024).decode())

#send test data to server
#reading the input.txt file
f = open("input.txt","r")
s.send("Sending data from input.txt".encode())
for line in f:
  print(line," SENT")
  s.send(line.encode())

# close the connection
s.close()   
