import json 

def names():
    f = open("data.json")
    data = json.load(f)
    names = []
    for disease in data : 
        names.append(disease["name"])
    return names
def info(d) :
    f = open("data.json")
    data = json.load(f)
    for disease in data :
        if(disease["name"] == d) :
            return disease["General information"]["definition"]
        for s in disease["synonyms"] :
            if d == s : 
                return disease["General information"]["definition"]

    f.close()

def symptoms(d) :
    f = open("data.json")
    data = json.load(f)
    for disease in data :
        if(disease["name"] == d) :
            return disease["General information"]["Symptoms"]
    f.close()

def term(d) :
    f = open("data.json")
    data = json.load(f)
    for disease in data :
        if(disease["name"] == d) :
            return disease["General information"]["Long-term effect"]
    f.close()

def treatment(d) :
    f = open("data.json")
    data = json.load(f)
    for disease in data :
        if(disease["name"] == d) :
            return disease["Treatment"]
    
    f.close()

def locate(d):
    f = open("data.json")

    data = json.load(f)
    for disease in data :
        if(disease["name"] == d) :
            return True, disease["name"]
        for s in disease["synonyms"] :
            if d == s : 
                return True , disease["name"]

    f.close()
    return False, None

def ask(question) :
    print(question)
    x = input()
    return x

def other() :
    print("I am not intelligent enough to answer your question. our 24/7 available customer server team will be happy to answer it if you wish to provide your email dow below:")
    email = input().split("@")[0]
    print("Alright, thank you for connecting with me "+ email + ". Have a good day!")

def is_disease(answer) :
    category = ""
    b = False
    n = ""
    for word in answer.split() :
        if word == "symptoms" or word == "definition" or word == "term" or word == "prevention" or word == "treatment" :
            category = word
        
        is_in_data , name = locate(word)
        if(is_in_data) : 
            b = True
            n = name
        
        if word == "info" :
            category = "info"
    
    return b, n, category



def analyse(sentence) : 
    words = sentence.split()
    for word in words :
        w = word.lower() 
        #if disease
        is_in_data, name = locate(w)
        if(is_in_data):
            print(info(w))
            print()
            print("What do you want to know about " + w + ". Choose one of the follow options")
            print("Symptoms")
            print("Long-term effect")
            print("Treatment")
            print("Other")
            print()
            answer = input()
            for a in answer.split() : 
                l = a.lower()
                if l == "symptoms" :
                    print(symptoms(name))
                elif l == "term" or l == "effect" :
                    print(term(w))
                elif l == "treatment" :
                    print(symptoms(name))
                elif l == "other" :
                    print(other())
                    

        #
        else : 
            other()



            
    