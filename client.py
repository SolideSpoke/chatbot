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
#understand want the server expect
def question(callback) : 
    b, n, cat = tools.is_disease()
    #talking about a specific diseases
    if b : 
        if cat == "" : 
            print("What do you want to know about" + name)

def s(question) : 
    while question != "" : 
        a = tools.ask(question)
        callback = send(a)
        question = str.encode(callback)

def username():
    name = input("What's your name")

s("What do you want to know about the folowing disases ?")
    