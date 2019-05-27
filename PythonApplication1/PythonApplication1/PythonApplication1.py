
#TCP/IP chat app

import socket
import sys

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind is used to associate the socket to the server address
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen puts the socket into server mode
# Accept() waits for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    #accept() returns an open connection between the server and client
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            #Data is read from the connection with recv() and transmitted with sendall()
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    #When the communication with a client is finished, the connection need to be clean up using close()        
    finally: #try:finally block ensures that close() is always called, even in the event of an error
        # Clean up the connection
        connection.close()