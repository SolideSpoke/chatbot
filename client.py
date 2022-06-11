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
            println("What do you want to know about" + name)

def run(question) : 
    while question != "" : 
        try :
            callback = send(question)
            question = callback
            question = tools.ask(question)
            if(question == "close") : 
                send("close") #close the server
                return None
        except ConnectionRefusedError :
            question = "Server unreachable, check your connexion"

def username():
    name = input("What's your name")

run("init")
    