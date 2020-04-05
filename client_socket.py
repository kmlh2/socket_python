from functions import send_text, get_text

def clientSocket(mySocket):
    serverIp = input("Welcome to socket client\nType a server ip: ")
    mySocket.connect((serverIp, 6666))
    print("Connected")

    #data = mySocket.recv(1024)
    #print(data.decode())
    arrivalMessage = next(get_text(mySocket))
    print(arrivalMessage)

    sendMessage = "CLIENT say: Hello Server"
    #mySocket.send(sendMessage.encode())
    send_text(mySocket, sendMessage)

    mySocket.close()