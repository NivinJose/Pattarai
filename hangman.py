import random
def hangman():
    
    a=["pattarai","engineering","loyola","nungambakkam"]
    b=random.choice(a)
    t=10
    g=' '
    c=set("abcdefghijklmnopqrstuvwxyz")
    
    while len(b)>0:
        main=""
        
        for letter in b:
            if letter in g:
                main=main+letter
            else:
                main=main+"_ "
                
        if main==b:
            print(main)
            print("-----------------------")
            print("YOU HAVE GOT IT RIGHT")
            print("CONGRATULATIONS")
            break
        
        print("GUESS THE WORDS",main)
        guess=input()
        
        if guess in c:
            g=g+guess
        else:
            print("ENTER A VALID CHARACTER")
            guess=input()
            
        if guess not in b:
            t=t-1
            if t==9:
                print("9 turns left")
                print("-----------------------")
            if t==8:
                print("8 turns left")
                print("-----------------------")
                print("           O           ")
            if t==7:
                print("7 turns left")
                print("-----------------------")
                print("           O           ")
                print("           |           ")
            if t==6:
                print("6 turns left")
                print("-----------------------")
                print("           O           ")
                print("           |           ")
                print("          /            ")
            if t==5:
                print("5 turns left")
                print("-----------------------")
                print("           O           ")
                print("           |           ")
                print("          / \          ")
            if t==4:
                print("4 turns left")
                print("-----------------------")
                print("          \O           ")
                print("           |           ")
                print("          / \          ")
            if t==3:
                print("3 turns left")
                print("-----------------------")
                print("          \O/          ")
                print("           |           ")
                print("          / \          ")
            if t==2:
                print("2 turns left")
                print("-----------------------")       
                print("          \O/ |        ")
                print("           |           ")
                print("          / \          ")
            if t==1:
                print("Final chance but you can")
                print("-----------------------")       
                print("          \O/_|        ")
                print("           |           ")
                print("          / \          ")
            if t==0:
                print("I FEEL SORRY FOR YOU")
                print("THE MAN IS NO MORE")
                print("-----------------------")       
                print("           O_|         ")
                print("          /|\          ")
                print("          / \          ")
                break
n=input("ENTER YOU NAME: ")
print("WELCOME",n)
print("---------------------")
print("TRY TO GUESS THE WORD WITH 10 CHANCES")
hangman()
