#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)
    

    while True:
        #Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() 
        #print(f"incoming request from {addr}")
        try:
            message = connectionSocket.recv(2048).decode()
            filename = message.split()[1]
            f = open(filename[1:], 'r')
            outputdata = f.read()

            #Send one HTTP header line into socket
            headerline = "HTTP 200 OK"
            connectionSocket.send(headerline.encode())


            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            error = "HTTP 404 Not Found"
            connectionSocket.send(error.encode())

            #Close client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
