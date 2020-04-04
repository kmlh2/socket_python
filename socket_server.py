import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.15", 6666))
server_socket.listen()
print("Waiting for connection")
connection_socket, address = server_socket.accept()
print("Client connected")
message = "SERVER say: Hello " + str(address)
connection_socket.send(message.encode())

data = connection_socket.recv(1024)
print(data.decode())

connection_socket.close()
server_socket.close()