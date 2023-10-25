#mots de passe validator

MotDePasse = input("Veuillez saisir votre mot de passe ")
long = len(MotDePasse)
if long <=8:
    print("Votre mot de passe est trop court")
elif long >9 and long <13:
    print("Votre mot de passe est acceptable")
elif long >14 and long < 17:
    print("Votre mot de passe est fort")
else:
    print("Votre mot de passe est  tres fort")