import zmq

# creating context
context = zmq.Context()

# creating subscriber socket
socket = context.socket(zmq.SUB)

# connecting to port and ip  that publisher bind.
socket.connect('tcp://127.0.0.1:2000')

# subscribing  to topic which  publisher publish
socket.setsockopt_string(zmq.SUBSCRIBE, 'Folder')

# subscribing to contents repeatedly
while True:
    # just receiving files from publisher  with the socket.recv() method
    files = socket.recv()

    # just formatting output format
    files = files.decode("utf-8")

    # printing the contents
    print(files)
