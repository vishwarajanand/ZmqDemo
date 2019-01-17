import zmq
import sys
import os

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")
# ipcPath=os.getcwd()+"/tmp.txt"
# sock.bind("ipc://"+ipcPath)

# print (" ".join(sys.argv[1:]))
x = " ".join(sys.argv[1:])
# Send a "message" using the socket
sock.send_string(x)
print (sock.recv())
