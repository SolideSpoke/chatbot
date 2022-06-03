import socket
import tools

HOST = "localhost"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def send(msg) :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str.encode(msg))
        data = s.recv(1024)
        return data.decode()
    
#send(name)
#print(f"Received {data!r}")

def s() : 
    a = tools.ask("What do you want to know one of this following diseses ? ")
    callback = send(a)
    print("from server : "+ callback)

def username():
    name = input("What's your name")

s()
    