from functions import send_text, get_text

def serverSocket(mySocket):
    mySocket.bind(("192.168.0.14", 6666))
    mySocket.listen()
    print("Welcome to server socket\nWaiting for connection")

    connection_socket, address = mySocket.accept()
    print("Client connected")
    sendMessage = "SERVER say: Hello " + str(address)
    #connection_socket.send(sendMessage.encode())
    send_text(connection_socket, sendMessage)

    # data = connection_socket.recv(1024)
    # print(data.decode())
    arrivalMessage = next(get_text(connection_socket))
    print(arrivalMessage)

    connection_socket.close()
    mySocket.close()