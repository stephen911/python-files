import server

HOST = "127.0.0.1"
PORT = 65432

with server.server(server.AF_INET, server.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        msg_client = input("client: ")
        client.sendall(msg_client.encode())

        data = client.recv(1024)
        print(data.decode())

    with conn:
        while True:
            pass