import random

def devinette():
    print("Veuillez entrer un nombre de votre choix:")
    x=int(input())
    nombre_cible = random.randint(1, 22)
    b=0
    while b<10:
        if b>0:
            x=int(input())    
        b+=1    
        if x!=nombre_cible:
            if x<nombre_cible:
                print("T'ES PRESQUE mais le nombre cible est plus grand\n")
            else:
                print("T'ES PRESQUE mais le nombre cible est plus petit\n")
        else:
            print("YOU WIN x)\n")
            break  
    
    if b==10:
        print("YOU LOSE x(\n")

print("Bienvenue dans le jeu de devinette !!\n")
devinette()
print("ARIGATO D'AVOIR JOUER AVEC NOUS !!\n")
