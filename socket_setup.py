import socket
from socket_server import serverSocket
from client_socket import clientSocket

socket_type = input("Choose a socket type...\nFor select a server socket enter s or for select a client socket enter c (S/c): ")

if socket_type.lower() == "s":
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket(my_socket)
elif socket_type.lower() == "c":
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket(my_socket)
elif socket_type == "":
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket(my_socket)
else:
    print("Invalid input, bye bye")


