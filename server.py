import socket


HOST = "localhost"
PORT = 65432

username = ""
def start() :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.bind((HOST, PORT))
        s.listen()
        while True :
            #print("What's your name ?")
            
            conn, addr = s.accept()
            with conn : 
                print(f"Connected by {addr}")
                while True : 
                    data = conn.recv(1024)
                    if not data : 
                        break
                    if data == b"close" : 
                        return None
                    
                    #username = data
                    d = data.decode()
                    print(d)

                    conn.sendall(data)

start()