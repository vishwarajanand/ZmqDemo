import zmq
import os

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")
# ipcPath=os.getcwd()+"/tmp.txt"
# sock.bind("ipc://"+ipcPath)

# Run a simple "Echo" server
while True:
    message = sock.recv().decode("utf-8") 
    sock.send_string("Echoed: " + message)
    print ("Echo: " + message)
