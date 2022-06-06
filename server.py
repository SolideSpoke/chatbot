import socket
import tools

HOST = "localhost"
PORT = 65432

username = ""
mind = ""
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

                    disease, name, category = tools.is_disease(d)
                    question = ""
                    if name != "" : 
                        mind = name
                    elif name == "" and category != "" and mind != "":
                        name = mind
                    if name != "" : 
                        if category == "symptoms" :
                            question = tools.symptoms(name)
                        elif category == "term" : 
                            question = tools.term(name)
                        elif category == "treatment" : 
                            question = tools.treatment(name)
                        else:
                            question = "What do you want to know about " + name
                            mind = name
                    elif category == "info" or category == "other":
                        mind = "info"
                        question = "Our 24/7 available customer server team will be happy to answer it if you wish to provide your email dow below:"
                    elif mind == "info" :
                        username = d.split("@")[0]
                        question = "Alright, thank you for connecting with me "+ username + ". Have a good day!"
                    else : 
                        mind = ""
                        question = "Can you repeat ?"
                    callback = str.encode(question)
                    print(callback)
                    conn.sendall(callback)

start()