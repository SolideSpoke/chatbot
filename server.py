import socket


HOST = "localhost"
PORT = 65432

def start() :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.bind((HOST, PORT))
        s.listen()
        while True :
            print("Server waiting for the client")
            
            conn, addr = s.accept()
            with conn : 
                print(f"Connected by {addr}")
                while True : 
                    data = conn.recv(1024)
                    if not data : 
                        break
                    if data == b"close" : 
                        return None
                    print(data)
                    conn.sendall(data)

start()