import socket
import  urllib.request, urllib.parse, urllib.error
HOST = "data.pr4e.org"
PORT = 80
  
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print((data.decode()))
mysock.close()


    # socket.bind(HOST, PORT)
    # socket.listen()
    # conn, addr = socket.accept()
    # print("connected with client: {}".format(addr))
    #
    # with conn:
    #     while True:
    #         data = conn.recv(1024)
    #         print(data.decode())
    #
    #         msg_server = input("server: ")
    #         conn.sendall(msg_server.encode())