import socket
import tools

HOST = "localhost"
PORT = 65432

username = ""
introduction = "What do you want to know about "
def start() :
    mind = ""
    mind_c = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        global introduction
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
                    
                    #is start 
                    if(d == "init") :
                        question = "Welcome message. What's your name"
                        mind_c = "username"
                    elif mind_c == "username" : 
                        username = d
                        mind_c = ""
                        question = "Nice to meet you aniss " + username + "\n What do you want to know about the following diseases ?"
                        for name in tools.names():
                            question += "\n-"+name                    
                    elif(d == "diseases list") :
                        question = "What do you want to know about the folowing disases ?" 
                        for name in tools.names() : 
                            question += "\n-" + name
                    else :
                        disease, name, category = tools.is_disease(d)
                        question = ""
                        if category == "info" : 
                            mind = ""
                            mind_c = "info"
                        elif category != "" :
                            mind_c = category
                        if name != "": 
                            mind = name
                        elif name == "" and category != "" and mind != "":
                            name = mind
                        if name != "" : 
                            if category == "" and mind_c != "" :
                                category = mind_c
                            if category == "symptoms" :
                                question = tools.symptoms(name)
                                mind_c = ""
                            elif category == "term" : 
                                question = tools.term(name)
                                mind_c = ""
                            elif category == "treatment" : 
                                question = tools.treatment(name)
                                mind_c = ""
                            else:
                                question = tools.definition(name)
                                question += "\n Please choose one of the following diseases " + name + "\n - Symptoms \n - Long-term effect \n - Treatment "
                                mind = name
                        elif name == "" and mind_c != "info" and mind != "": 
                            question = "Which diseases you want info about ?"
                        elif category == "info" or category == "other":
                            mind = "info"
                            question = "Our 24/7 available customer server team will be happy to answer it if you wish to provide your email dow below:"
                        elif mind == "info" :
                            username = d.split("@")[0]
                            question = "Alright, thank you for connecting with me "+ username + ". Have a good day! \n" + introduction
                            mind = ""
                        else : 
                            mind = ""
                            question = "Can you repeat ?"
                    callback = str.encode(question)
                    print(mind)
                    conn.sendall(callback)

start()