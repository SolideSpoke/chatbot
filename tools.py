import json 
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
            return True
        for s in disease["synonyms"] :
            if d == s : 
                return True

    f.close()
    return False
    
def analyse(sentence) : 
    words = sentence.split()
    for word in words :
        w = word.lower() 
        #if disease
        if(locate(w)):
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
                    print(symptoms(w))
                elif l == "term" or l == "effect" :
                    print(term(w))
                elif l == "treatment" :
                    print(symptoms(w))

        #
        else : 
            print("I am not intelligent enough to answer your question. our 24/7 available customer server team will be happy to answer it if you wish to provide your email dow below:")
            email = input().split("@")[0]
            print("Alright, thank you for connecting with me "+ email + ". Have a good day!")

analyse("info")
            
    