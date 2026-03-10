import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_ip = "192.168.1.18"
port = 5000

client_socket.connect((server_ip,port))

print("connected to server.....")

while True:
    message = input("Client: ")

    client_socket.send(message.encode())
    if message.lower() == "exit":
        print("bye bye....")
        break

    reply = client_socket.recv(1024).decode()
    print("Server: ",reply)

client_socket.close()