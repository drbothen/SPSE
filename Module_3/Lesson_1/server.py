import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind to address and Port
tcpSocket.bind(("0.0.0.0", 8000))


# set server to listen for connections
tcpSocket.listen(2)

print "Waiting for a Client ..."
# accept client connection. Will wait until client is connected
(client, (ip, port)) = tcpSocket.accept()
print "Recieved connection from: ", ip
print "Starting ECHO output"

#Creating data varible. This will hold data recieved from the client
data = "dummy"


# keep recieveing data from client
while len(data):
    
    data = client.recv(2048)
    print "Client sent: ",data
    client.send(data)

print "Closeing Connection ..."
client.close()

print "Shutting down server ..."

tcpSocket.close()
