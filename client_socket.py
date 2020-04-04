import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.15", 6666))
print("Connected")

data = client_socket.recv(1024)
print(data.decode())

message = "CLIENT say: Hello Server"
client_socket.send(message.encode())

client_socket.close()