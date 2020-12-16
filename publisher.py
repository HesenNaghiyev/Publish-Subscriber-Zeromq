import zmq
import os
from time import sleep

# Ask for directory path
print("Please Enter the Folder Name: ")

# Getting input from user
DIRECTORY_PATH = input()

# creating context
context = zmq.Context()

# creating publisher socket
socket = context.socket(zmq.PUB)

# binding ip, port  and protocol for socket
socket.bind('tcp://127.0.0.1:2000')

# while is used for repeatedly publishing, 
while True:
    # getting all files according to path that user entered as an input
    files = os.listdir(DIRECTORY_PATH)

    # looping through all files
    for file in files:
        file = ' has '+file
        # sending these files in the format of Path + File
        socket.send_string('Folder ' + os.path.abspath(os.path.join(DIRECTORY_PATH, file)))

        # publishing the contents in every 5 seconds
    sleep(5)
