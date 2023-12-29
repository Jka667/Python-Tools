
#devinette de nombre 
import random
print("================Bienvenue dans le jeu de devinette de nombres !================")
NombreMagic = random.randint(0,9999)
Aleatoire = int(input("Veuillez saisir votre proposition  >>>>>>>>>>>>>>>"))

while  Aleatoire != NombreMagic:
 if Aleatoire< NombreMagic:   
    print ("Le nombre a deviner est plus grand,Augmentez ")
    Aleatoire = int(input("Veuillez saisir votre proposition "))

 elif Aleatoire > NombreMagic:
    print ("Le nombre a deviner est plus petit, Diminuez  ")
    Aleatoire = int(input("Veuillez saisir votre proposition "))
 else:  Aleatoire = NombreMagic
   
print("Fellicitation vous avez trouvez le nombre exact qui est ", NombreMagic)
   
