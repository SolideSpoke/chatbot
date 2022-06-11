import socket
import tools

HOST = "localhost"
PORT = 65432

username = ""

def start() :
    mind = ""
    mind_c = ""

    #initialization of the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        global introduction
        s.bind((HOST, PORT))
        s.listen()

        while True :
            conn, addr = s.accept()
            with conn : 
                print(f"Connected by {addr}")
                while True : 
                    data = conn.recv(1024)
                    if not data : 
                        break
                    if data == b"close" : 
                        return None
                    d = data.decode()
                    
                    #initialization of the conversation  
                    if(d == "init") :
                        question = "Hello what's your name ?"
                        mind_c = "username"
                    elif mind_c == "username" : 
                        username = d
                        mind_c = ""
                        question = "Hi " + username + ", I'm Lina, and I'll hopefully be answering any medical questions that you have."
                        question += "Please ask me anything relating to medical diseases. My answers come from the World Health Organization and Center for Disease Control and Prevention: "
                        for name in tools.names():
                            question += "\n-"+name           
                    elif(d == "diseases list") :
                        question = "Please ask me anything relating to medical diseases. My answers come from the World Health Organization and Center for Disease Control and Prevention."
                        question += "\n What else would you like to know about the folowing diseases ?" 
                        for name in tools.names() : 
                            question += "\n-" + name

                    #body of the conversation
                    else :
                        disease, name, category = tools.is_disease(d.lower())
                        question = ""
                        if category == "information" : 
                            mind = ""
                            mind_c = "information"
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
                            elif category == "prevention" :
                                question = tools.prevention(name)
                                mind_c = ""
                            else:
                                question = tools.definition(name)
                                question += "\n Please choose one of the following diseases: " + name + "\n - Symptoms \n - Long-term effect \n - Treatment \n - Prevention"
                                mind = name
                        elif name == "" and mind_c != "info" and category != "": 
                            question = "Sorry, can you please tell me which disease are you talking about ?"
                        elif category == "information" or category == "other":
                            mind = "information"
                            question = "Our 24/7 available customer server team will be happy to answer it if you wish to provide your email dow below:"
                        elif mind == "information" :
                            username = d.split("@")[0]
                            question = "Alright, thank you for connecting with me "+ username + ". Have a good day! \n" + introduction
                            mind = ""
                        else : 
                            mind = ""
                            question = "Sorry can you repeat what you just said ?"

                    #sending the answer to the client
                    callback = str.encode(question)
                    print(mind)
                    conn.sendall(callback)

start()