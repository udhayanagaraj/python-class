import socket


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "0.0.0.0"
port = 5000


server_socket.bind((host,port))

server_socket.listen(1)

print("Server waiting for connection......")

conn,addr = server_socket.accept()

print("Connected to: ",addr)

while True:
    message = conn.recv(1024).decode()

    if message.lower() == "exit":
        print("Client disconnected")
        break

    print("Client: ",message)

    reply = input("Server: ")
    conn.send(reply.encode())


conn.close()
server_socket.close()
